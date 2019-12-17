import requests
from flask import Flask, escape, url_for, request, render_template

app = Flask(__name__)
addr = 'http://10.144.71.51:5000'
func_url = addr + '/api/web_page'

@app.route('/')
def index():
    return render_template('parentData.html')

@app.route('/', methods = ['POST'])
def getData():
    data = []
    data.append(request.form['CAR NUMBER'])
    data.append(request.form['PHONE NUMBER'])
    data_string = ','.join(data)
    response = requests.post(func_url, data=data_string)

    return data_string



if __name__ == '__main__':
    app.run(debug=True)
