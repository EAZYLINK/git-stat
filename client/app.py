from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('/signup.html')
    if request.method == 'POST':
        data = request.form
        response = requests.post('http://127.0.0.1:8000/api/v1/auth/signup', data)
        return response.content

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/login.html')
    if request.method == 'POST':
        data = request.form
        response = requests.post('http://127.0.0.1:8000/api/v1/auth/login', data)
        return render_template('/commits.html', username=response.text)

@app.route('/commits')
def commits():
    return render_template('/commits.html')

if __name__ == '__main__':
    app.run(debug=True)