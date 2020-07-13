from flask import Flask, request, jsonify, url_for, redirect, send_file, render_template, json
from datetime import date
import os
import dataAnalyze as da
import utils as ut
import subprocess
from config import HTML_PATH, SPIDER_PATH, DATA_PATH, IMAGE_PATH, PORT

existing_ranking = None
today_date = ""


app = Flask(__name__, static_folder='data/static', template_folder='data/static/templates')


@app.route('/favicon.ico', methods=['GET'])
def ico():
    return url_for('static', filename='images/icon.png')


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


@app.route('/dashboard/ranking', methods=['GET'])
def rank():
    global existing_ranking
    global today_date

    if request.method == 'GET':
        if date.today() != today_date:
            today_date = str(date.today())
            table_name = 'corona_data_' + today_date.replace('-', '_')
            existing_ranking = da.topCountries(table_name)
        
        return jsonify(existing_ranking)


@app.route('/dashboard/searchCountry', methods=['GET', 'POST'])
def listCountry():
    if request.method == 'GET':
        return ut.getHTML(HTML_PATH + 'dashboard_searchCountry.html')
    elif request.method == 'POST':
        country_code = request.form['countries']
        img_name = country_code + '.png'
        return ut.getHTML(HTML_PATH + 'dashboard_searchCountry.html') + '\n<Image src="' + IMAGE_PATH + img_name + '">'

app.run(port=PORT)
