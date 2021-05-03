from flask import Flask
from flask import render_template
from flask import request
import boto3

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name
'''
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)
'''

@app.route('/')
def index():
    users = [ 'Rosalia','Adrianna','Victoria','Mihad','Angelina' ]
    #ec2 = boto3.resource('ec2')
    #return ec2.instances.all()
    #return 'hello world'
    return render_template('index.html', title='Welcome', members=users)

@app.route('/instances')
def instances():
   ec2_resource = boto3.client('ec2')
   response = ec2_resource.describe_instances()
   instances = []
   for reservation in response['Reservations']:
    for instance in reservation['Instances']:
      instances.append(f"Instance Id: {instance['InstanceId']} | Instance Type: {instance['InstanceType']} | Monitoring State: {instance['Monitoring']['State']}")
   obj = {'Instances': instances}
   # for x in obj['Instances']:
   #    print(x)
   return render_template('instances.html', title='EC2 Instances', instances=obj)
   


app.run(host='0.0.0.0', port=81)
