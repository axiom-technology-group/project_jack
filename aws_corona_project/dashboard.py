from flask import Flask, request, jsonify, url_for, redirect, send_file, render_template, json, send_from_directory
from datetime import date
import os
import dataAnalyze as da
import utils as ut
import subprocess
from config import HTML_PATH, SPIDER_PATH, DATA_PATH, IMAGE_PATH, PORT


existing_summary = None
today_date = ''
today_table = None


app = Flask(__name__, static_folder='data/static', template_folder='data/static/templates')


@app.route('/favicon.ico', methods=['GET'])
def ico():
    return url_for('static', filename='images/icon.png')


@app.route('/download_file/<file_name>', methods=['GET'])
def download_file(file_name):

    return send_from_directory('data\\static\\data\\', filename=file_name)


@app.route('/', methods=['GET'])
def main():
    return render_template('dashboard.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')
    elif request.method == 'POST':
        country_code = request.form['searched_countries']
        country_name = da.getName(country_code)
        selected_countries = 'static/images/' + country_code + '.png'

        return render_template('dashboard_search.html', imgfile=selected_countries, selection=country_name)

    return render_template('dashboard.html')


@app.route('/dashboard/summary', methods=['GET'])
def rank():
    global existing_summary
    global today_date

    if request.method == 'GET':
        if date.today() != today_date:
            today_date = str(date.today())
            table_name = 'corona_data_' + today_date.replace('-', '_')
            existing_summary = da.getTotal()
        
        return jsonify(existing_summary)


@app.route('/dashboard/table_today', methods=['GET'])
def table_today():
    global today_date
    global today_table

    if request.method == 'GET':
        table = list()

        if today_date != date.today():
            csv_name = DATA_PATH + ut.getTableName()

            f = open(csv_name)
            lines = f.readlines()
            columns = lines[0].lower().replace(
                ' ', '_').replace('/', '_').split(',')[1:]
            columns[9] = 'tot_cases_1m_pop'
            lines = lines[1:]

            for line in lines:
                table.append(da.mergeDict(columns, line.split(',')[1:], insert_img=True))
            
            today_table = table
        
        return jsonify(table)


app.run(port=PORT)
