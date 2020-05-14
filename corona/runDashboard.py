from flask import Flask, url_for, request, redirect, render_template
import myRE as re
import os
import sys

app = Flask(__name__)
html_path = 'C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/'

@app.route('/')
def goToMainPage():
    return re.getHTML(html_path + 'dashboard.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    command = request.form['commands']
    html = re.getHTML(
        'C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard.html')
    if command == 'craw_data':
        try:
            os.system(
                'scrapy runspider C:/Users/zhan1/Desktop/Python/project_jack/corona/corona_spider.py')
        except:
            return html + '<p>Failed to excute</p>'
        return html + 'done'
    elif command == 'exit':
        re.tryexit()
        return 'still herer'
    else:
        return html

def click():
    return re.getHTML('C:/Users/zhan1/Desktop/Python/project_jack/corona/htmls/dashboard.html') + 'click'

app.run(port=9999, debug=True)
