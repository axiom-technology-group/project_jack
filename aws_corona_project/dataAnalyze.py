import urllib.request as request
import psycopg2
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import utils as ut
from myClasses import Country
from config import FLAG_PATH, PSQL_PORT


def uploadData(upload_file, port=PSQL_PORT, table_name='default', data=''):
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
        columns = lines[0].replace('/', '_').replace(' ', '_').lower()[2:]
        columns_list = columns.split(',')

        if date == '':
            table_name = 'corona_data_' + ut.getDate().replace('-', '_')
        else:
            table_name = 'corona_data_' + date
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
            del data[0]
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


def generateGraph(input_csv, file_path, port=PSQL_PORT, columns=['Country/Other', 'Total Cases'], upload=False):
    sns.set(style='whitegrid')
    data = pd.read_csv(input_csv, encoding='ISO-8859-1')
    data = data[columns][data['Total Cases'] > 5000].sort_values(by='Total Cases', ascending=False)
    f, ax = plt.subplots(figsize=(10, 20))
    sns.barplot(x='Total Cases', y='Country/Other', data=data)
    plt.title('COVID-19 Confirmed Cases')
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Country')
    plt.show()
    file_name = file_path + \
        ut.getDate() + 'COVID-19_Confirmed_Cases.png'
    plt.savefig(file_name)
    if upload:
        uploadData(file_name, port, 'corona_img')


def selectData(table_name, port=PSQL_PORT, column=['*'], condition=''):
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
    return [desc for desc in records]


def generateDF(column_list, data_list):
    output = {'type': [], 'data': []}
    for i in range(len(column_list)):
        if data_list[i] != 'N/A':
            try:
                data_list[i] = int(data_list[i])
                output['type'].append(column_list[i])
                output['data'].append(data_list[i])
            except:
                pass
    df = pd.DataFrame(data=output)

    return df


def plotCountry(data, country, path):
    column_names = 'Country/Other,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious/Critical,Tot Cases/1M pop,Deaths/1M pop,Total Tests,Test/1M Pop,Continent'

    df = generateDF(column_names.split(','), data)

    sns.set()
    sns.barplot(x='type', y='data', data=df)
    plt.xticks(rotation=45)
    plt.savefig(path + country + '.png')


def topCountries(table_name, port=PSQL_PORT, top=3):
    top_list = selectData(table_name, port)[0:top]
    top_countries = list()
    for i in range(len(top_list)):
        top_countries.append(top_list[i][0])
    dics = [e.value for e in Country]

    for item in dics:
        for i in range(len(top_countries)):
            if top_countries[i] == item['Name'] or top_countries[i] == item['Code']:
                input_dict = dict()
                input_dict['Name'] = item['Name']
                input_dict['Flag'] = 'static/flags/' + str(getFlag(item['Name']))
                top_countries[i] = input_dict

    return top_countries


def getColumnNames(table_name, port=PSQL_PORT):
    search_query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '" + table_name + "';"

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
    cursor.execute(search_query)
    records = cursor.fetchall()

    return [desc[0] for desc in records]


def mergeDict(columns, data, insert_img=False):
    if len(columns) != len(data):
        raise ValueError('Different length')

    output = dict()
    for i in range(len(columns)):
        output[columns[i]] = data[i]
        if insert_img:
            country = data[0]
            flag = getFlag(country)
            if flag == -1:
                output['flag'] = 'static/flags/-1.png'
            else:
                output['flag'] = 'static/flags/' + str(getFlag(country))
    
    return output


def getFlag(country_name):
    dics = [e.value for e in Country]
    country = country_name.lower()

    for item in dics:
        if item['Name'].lower() == country or item['Code'].lower() == country:
            return item['Flag']
        elif 'special' in item and item['special'].lower() == country:
            return item['Flag']

    return -1


def getName(country_code):
    dics = [e.value for e in Country]

    for item in dics:
        if item['Code'] == country_code:
            return item['Name']

    return -1


def getTotal(date=''):
    output = dict()
    total_cases = selectData(ut.getTableName(version='psql', date=date), column=['total_cases'])
    total_cases = [int(item[0]) for item in total_cases]
    output['total_cases'] = sum(total_cases)

    death = [item[0] for item in selectData(
        ut.getTableName(version='psql', date=date), column=['total_deaths'])]
    death = list(filter(lambda str: str != 'N/A' and str != '', death))
    death = [int(item) for item in death]
    output['total_death'] = sum(death)

    new_cases = selectData(ut.getTableName(
        version='psql', date=date), column=['new_cases'])
    new_cases = [(item[0])[1:] for item in new_cases]
    new_cases = list(filter(lambda str: str != '/A' and str != '', new_cases))
    new_cases = [int(item) for item in new_cases]
    output['new_cases'] = sum(new_cases)

    recovery = [item[0] for item in selectData(ut.getTableName(
        version='psql', date=date), column=['total_recovered'])]
    recovery = list(filter(lambda str: str != 'N/A' and str != '', recovery))
    recovery = [int(item) for item in recovery]
    output['total_recovered'] = sum(recovery)
    
    return output


