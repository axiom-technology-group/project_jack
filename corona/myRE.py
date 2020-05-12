import datetime
import subprocess
import urllib.request as request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import PyPDF2
import psycopg2
import fpdf
import logging
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def findAll(file, item):
    """
    This function will find the item in the file
    with the correct given file path and file
    name, and return a count of item in each row.
    """
    with open(file) as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if item in line:
                count += 1
        f.close()
    return count

def getDate():
    """
    This function will return a string with
    proper date format.
    """
    now = datetime.date.today()
    return str(now)


def countWords(page, file_type='web', give_graph=False, include_stopwords=False, language='english'):
    """
    This function will count the words in a webpage or pdf
    and return a list containing the word counts for each
    word. (mode 'g' for providing graph)
    """
    if file_type == 'web': 
        reponse = request.urlopen(page)
        soup = BeautifulSoup(reponse.read(), 'html5lib')
        text = soup.get_text(strip=True)
    elif file_type == 'pdf':
        f = open(page, 'rb')
        pdf = PyPDF2.PdfFileReader(f)
        text = ''
    
        for i in range(pdf.numPages):
            text += pdf.getPage(i).extractText()
        f.close()

    tokens = [t for t in text.split()]
    clean = tokens[:]

    if include_stopwords is False:
        for token in tokens:
            if token in stopwords.words(language):
                clean.remove(token)
    freq = nltk.FreqDist(clean)
    
    if give_graph is True:
        freq.plot(20, cumulative=True)
    return freq.items()


def csvToJson(file_name):
    """
    This function will be able to turn csv file
    into Json file
    """
    input_csv = open(file_name, 'r')
    file_name = file_name.replace('.csv', '.json')
    output_json = open(file_name, 'w')

    output_json.write('{\n')
    output_json.write('\t"date": ' + '"' + getDate() + '"' + ',\n')
    lines = input_csv.readlines()
    types = lines[0].split(',')
    
    i = 1
    for i in range(len(lines)):
        data = lines[i].split(',')
        for x in range(len(types)):
            if x == 0:
                output_json.write('\t "' + data[0] + '": {\n')
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


def uploadData(upload_file, port, table_name):
    connection = psycopg2.connect(user='postgres', 
                                        password='qwertyuiop135', 
                                        host='127.0.0.1', 
                                        port=port,
                                        database='postgres')
    cursor = connection.cursor()
    if upload_file.endswith('csv'):
        f = open(upload_file, 'r')
        lines = f.readlines()
        f.close()
        columns = lines[0].replace('/', '_').replace(' ', '_').lower()
        columns_list = columns.split(',')

        cursor.execute("SELECT * FROM " + table_name)
        existing_column = [desc[0] for desc in cursor.description]
        
        if not all(elem in columns_list for elem in existing_column):
            column_query = 'ALTER TABLE ' + table_name
            for column in columns_list:
                if column not in existing_column:
                    column_query += ' ADD COLUMN ' + column + ' text,'
            column_query = column_query[:-1] + ';'
            cursor.execute(column_query)

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
        getDate() + 'COVID-19_Confirmed_Cases.png'
    plt.savefig(file_name, bbox_inches='tight')
    if upload:
        uploadData(file_name, 5000, 'corona_img')


def getHTML(file_path):
    f = open(file_path)
    html = f.read()
    f.close()
    return html

