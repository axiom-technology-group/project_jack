import datetime
import subprocess
import urllib.request as request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import PyPDF2
import psycopg2
import fpdf
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from myClasses import MyLogging


def goLog(
        log_path, script, level='info', mode='w', max_size=10000000):
    """
    This function will help other program to log what they did
    or error messages. 
    """
    if not os.path.exists(log_path):
        raise FileNotFoundError('Path does not exist.')

    try:
        os.makedirs(log_path + 'log/')
    except FileExistsError:
        mode = 'a'
    log_path = log_path + 'log/'

    list_file = list(filter(lambda file: file.endswith(
        '.log'), os.listdir(log_path)))
    if len(list_file) == 0:
        file_name = 'AWS.ZHANZ1.DATA_log_01.log'
    else:
        last_file = list_file[len(list_file) - 1]
        if os.path.getsize(log_path + last_file) < max_size:
            file_name = last_file
        else:
            current_num1 = int(last_file[20])
            current_num2 = int(last_file[21])
            if (current_num2 + 1) == 10:
                current_num1 += 1
                current_num2 = 0
            else:
                current_num2 += 1
            num = str(current_num1) + str(current_num2)
            file_name = 'AWS.ZHANZ1.DATA_log_' + num + '.log'

    MyLog = MyLogging()
    MyLog.basicConfig(filename=log_path+file_name, filemode=mode, level=20)
    MyLog.log(level, script)


def getDate():
    """
    This function will return a string with
    proper date format.
    """
    now = datetime.date.today()
    return str(now)


def csvToJson(file_name):
    """
    This function will be able to turn csv file
    into Json file
    """
    try:
        input_csv = open(file_name, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist')
    except IOError:
        raise IOError('Failed to read the file')
    file_name = file_name.replace('.csv', '.json')
    output_json = open(file_name, 'w')

    output_json.write('{\n')
    output_json.write('\t"date": ' + '"' + getDate() + '"' + ',\n')
    lines = input_csv.readlines()
    types = lines[0].split(',')
    
    for i in range(1, len(lines)):
        data = lines[i].split(',')
        for x in range(len(types)):
            if x == 0:
                output_json.write('\t "' + data[0] + '": {\n')
            elif x == (len(types) - 1):
                output_json.write(
                    '\t\t"' + types[x].strip() + '": ' + '"' + data[x].strip() + '"\n')
            else:
                output_json.write('\t\t"' + types[x].strip() + '": ' + '"' + data[x].strip() + '"' + ',\n')
        output_json.write('\t},\n')
    output_json.write('}')
    input_csv.close()
    output_json.close()


def prepareData(input_list):
    if len(input_list) == 0:
        return ''
    else:
        output = ''
        for i in range(len(input_list) - 1):
            output += "'" + str(input_list[i]).replace(' ', '_') + "', "
        return output + "'" + input_list[len(input_list) - 1] + "'"


def uploadData(upload_file, port, table_name='default', log_path='C:/Users/zhan1/Desktop/Python/project_jack/corona/'):
    try:
        psycopg2.connect(user='postgres', 
                        password='qwertyuiop135', 
                        host='127.0.0.1', 
                        port=port,
                        database='postgres')
    except:
        goLog(log_path, 'PostgresSQL_uploadData: Failed to connect to PSQL', level='error')
        quit
    
    connection = psycopg2.connect(user='postgres',
                                  password='qwertyuiop135',
                                  host='127.0.0.1',
                                  port=port,
                                  database='postgres')
    cursor = connection.cursor()

    if upload_file.endswith('csv'):
        try:
            f = open(upload_file, 'r')
        except IOError:
            raise IOError('Cannot read the file.')
        lines = f.readlines()
        f.close()
        columns = lines[0].replace('/', '_').replace(' ', '_').lower()
        columns_list = columns.split(',')

        table_name = 'corona_data_' + getDate().replace('-', '_')
        create_table_query = 'CREATE TABLE ' + table_name + ' ('
        for column in columns_list:
            create_table_query += column + ' text NOT NULL,' 

        create_table_query = create_table_query[:-1] + ');'

        try:
            cursor.execute(create_table_query)
        except:
            goLog(
                log_path, 'PostgresSQL_uploadData: Failed to create table.', level='error')
            quit

        cursor.execute('SELECT * FROM ' + table_name)
        existing_column = [desc[0] for desc in cursor.description]

        datas = lines[1:]
        add_data_query = 'INSERT INTO ' + table_name + ' (' + columns + ')' + ' VALUES '

        for data in datas:
            data = data.split(',')
            data_query = '(' + prepareData(data) + ');'
            cursor.execute(add_data_query + data_query)

    elif upload_file.endswith('.png'):
        f = open(upload_file, 'rb')
        data = f.read()
        f.close()
        date = getDate()
        add_data_query = 'INSERT INTO ' + table_name + ' (date, img) VALUES (' + date + ', ' + str(psycopg2.Binary(data)) + ')'
        cursor.execute(add_data_query)

    goLog(log_path, 'PostgresSQL_uploadData: Successfully uploaded data to Database')
    connection.commit()  
    connection.close()


uploadData(
    'C:/Users/zhan1/Desktop/Python/project_jack/corona/2020-05-09-coronavirus.csv', 5000)

"""
connection = psycopg2.connect(user='postgres',
                              password='qwertyuiop135',
                              host='127.0.0.1',
                              port=5000,
                              database='postgres')
cursor = connection.cursor()
cursor.execute(
    "select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
f = cursor.fetchall()
print([name for tuples in f for name in tuples])
connection.close()
"""


def generateGraph(input_csv, columns=['Country/Other', 'Total Cases'], upload=False):
    sns.set(style='whitegrid')
    data = pd.read_csv(input_csv, encoding='ISO-8859-1')
    data = data[columns][data['Total Cases'] > 5000].sort_values(by='Total Cases', ascending=False)
    f, ax = plt.subplots(figsize=(10, 20))
    sns.barplot(x='Total Cases', y='Country/Other', data=data)
    plt.title('COVID-19 Confirmed Cases')
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Country')
    plt.show()
    file_name = 'C:/Users/zhan1/Desktop/Python/project_jack/corona/' + \
        getDate() + 'COVID-19_Confirmed_Cases.png'
    plt.savefig(file_name, bbox_inches='tight')
    if upload:
        uploadData(file_name, 5000, 'corona_img')


def getHTML(file_path):
    try:
        f = open(file_path)
    except:
        raise FileNotFoundError('File does not exist.')
    html = f.read()
    f.close()
    return html





