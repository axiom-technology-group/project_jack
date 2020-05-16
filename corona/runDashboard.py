from flask import Flask, request, jsonify, url_for, redirect
import os
import myRE as re
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return re.getHTML('C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        return re.getHTML('C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard.html')
    elif request.method == 'POST':
        command = request.form['commands']
        button_msg = request.form['button']

        if button_msg == 'craw':
            os.system(
                'scrapy runspider C:/Users/zhan1/Desktop/Python/project_jack/corona/corona_spider.py')
        elif button_msg == 'upload':
            re.uploadData(
                'C:/Users/zhan1/Desktop/Python/project_jack/corona/2020-05-11-coronavirus.csv', 5000)
        elif button_msg == 'console':
            return redirect('/dashboard/console')
        elif button_msg == 'search':
            return redirect('/dashboard/search')

    return re.getHTML('C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard.html') + 'finished'

@app.route('/dashboard/console', methods=['GET', 'POST'])
def console():
    if request.method == 'GET':
        return 'Welcome to console \n' + re.getHTML('C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard_console.html')
    elif request.method == 'POST':
        command = request.form['commands']
        msg = subprocess.run(command, capture_output=True, shell=True)
        return re.getHTML(
            'C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard_console.html') + '\n' + msg.stdout.decode()


@app.route('/dashboard/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return 'Searched Items:'
    elif request.method == 'POST':
        table_name = request.get_json()['table_name']
        column_name = request.get_json()['column_name']
        return str(re.selectData(table_name, 5000, column=column_name))


app.run(port=9999, debug=True)
