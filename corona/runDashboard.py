from flask import Flask, url_for, request, redirect, render_template
import myRE as re
import os
import sys

app = Flask(__name__)

@app.route('/')
def goToMainPage():
    f = open('C:/Users/zhan1/Desktop/Python/project_jack/htmls/dashboard.html')
    html = f.read()
    f.close()
    return html

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    command = request.form['commands']
    f = open('C:/Users/zhan1/Desktop/Python/project_jack/htmls/dashboard.html')
    html = f.read()
    f.close()
    if command == 'craw_data':
        try:
            os.system(
                'scrapy runspider C:/Users/zhan1/Desktop/Python/project_jack/corona/corona_spider.py')
        except:
            return html + '<p>Failed to excute</p>'
        return html + 'done'
    else:
        return html


app.run(port=9999)
