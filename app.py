from flask import Flask
from flask import render_template
from flask import request
import boto3

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

@app.route('/')
def index():
    users = [ 'Rosalia','Adrianna','Victoria','Mihad','Angelina' ]
    return render_template('index.html', title='Welcome', members=users)

app.run(host='0.0.0.0', port=81)
