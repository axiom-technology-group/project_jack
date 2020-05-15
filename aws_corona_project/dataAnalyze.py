import urllib.request as request
import psycopg2
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import utils as ut


def uploadData(upload_file, port, table_name='default'):
    try:
        psycopg2.connect(user='postgres', 
                        password='qwertyuiop135', 
                        host='127.0.0.1', 
                        port=port,
                        database='postgres')
    except:
        ut.goLog('PostgresSQL_uploadData: Failed to connect to PSQL', level='error')
        return
    
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

        table_name = 'corona_data_' + ut.getDate().replace('-', '_')
        create_table_query = 'CREATE TABLE ' + table_name + ' ('

        for column in columns_list:
            create_table_query += column + ' text NOT NULL,' 

        create_table_query = create_table_query[:-1] + ');'

        try:
            cursor.execute(create_table_query)
        except:
            ut.goLog('PostgresSQL_uploadData: Failed to create table.', level='error')
            return

        cursor.execute('SELECT * FROM ' + table_name)
        existing_column = [desc[0] for desc in cursor.description]

        datas = lines[1:]
        add_data_query = 'INSERT INTO ' + table_name + ' (' + columns + ')' + ' VALUES '

        for data in datas:
            data = data.split(',')
            data_query = '(' + ut.prepareData(data) + ');'
            cursor.execute(add_data_query + data_query)

    elif upload_file.endswith('.png'):
        f = open(upload_file, 'rb')
        data = f.read()
        f.close()
        date = ut.getDate()
        add_data_query = 'INSERT INTO ' + table_name + ' (date, img) VALUES (' + date + ', ' + str(psycopg2.Binary(data)) + ')'
        cursor.execute(add_data_query)

    ut.goLog('PostgresSQL_uploadData: Successfully uploaded data to Database')
    connection.commit()  
    connection.close()


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
        ut.getDate() + 'COVID-19_Confirmed_Cases.png'
    plt.savefig(file_name)
    if upload:
        uploadData(file_name, 5000, 'corona_img')


def selectData(table_name, port, column=['*'], condition=''):
    try:
        psycopg2.connect(user='postgres',
                         password='qwertyuiop135',
                         host='127.0.0.1',
                         port=port,
                         database='postgres')
    except:
        ut.goLog('PostgresSQL_selectData: Failed to connect to PSQL', level='error')
        return

    connection = psycopg2.connect(user='postgres',
                                  password='qwertyuiop135',
                                  host='127.0.0.1',
                                  port=port,
                                  database='postgres')
    cursor = connection.cursor()
    select_query = 'SELECT ' + ut.getList(column) + ' FROM ' + table_name

    if len(condition) != 0:
        select_query += ' WHERE ' + condition
    
    cursor.execute(select_query)
    records = cursor.fetchall()
    
    try:
        cursor.execute(select_query)
    except:
        ut.goLog('PostgresSQL_selectData: Failed to get PSQL', level='error')
        return

    ut.goLog('PostgresSQL_selectData: Successfully selected the data from table.')
    return [desc[0] for desc in records]

