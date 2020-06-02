from flask import Flask, request, jsonify, url_for, redirect, send_file
import os
import dataAnalyze as da
import utils as ut
import subprocess
from config import HTML_PATH, SPIDER_PATH, DATA_PATH

existing_ranking = None


app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return ut.getHTML(HTML_PATH + 'dashboard.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return ut.getHTML(HTML_PATH + 'dashboard.html')
    elif request.method == 'POST':
        command = request.form['commands']
        button_msg = request.form['button']

        if button_msg == 'craw':
            os.system(
                'scrapy runspider ' + SPIDER_PATH + 'corona_spider.py')
        elif button_msg == 'upload':
            da.uploadData(
                DATA_PATH + '2020-05-11-coronavirus.csv', 5000)
        elif button_msg == 'console':
            return redirect('/dashboard/console')
        elif button_msg == 'search':
            return redirect('/dashboard/search')

    return ut.getHTML(HTML_PATH + 'dashboard.html') + 'finished'


@app.route('/dashboard/console', methods=['GET', 'POST'])
def console():
    if request.method == 'GET':
        return 'Welcome to console \n' + ut.getHTML(HTML_PATH + 'dashboard_console.html')
    elif request.method == 'POST':
        command = request.form['commands']
        msg = subprocess.run(command, capture_output=True, shell=True)
        return ut.getHTML(
            HTML_PATH + 'dashboard_console.html') + '\n' + msg.stdout.decode()


@app.route('/dashboard/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'Searched Items:'
    elif request.method == 'POST':
        table_name = request.get_json()['table_name']
        column_name = request.get_json()['column_name']
        condition = request.get_json()['condition']
        return str(da.selectData(table_name, 5000, column=column_name, condition=condition))


@app.route('/dashboard/ranking', methods=['GET', 'POST'])
def rank():
    global existing_ranking
    if request.method == 'GET':
        images = [img[1] for img in existing_ranking]
        return send_file(images[0])
    elif request.method == 'POST':
        table_name = request.get_json()['table_name']
        existing_ranking = re.topCountries(table_name)
        return str(existing_ranking)


app.run(port=9999, debug=True)
