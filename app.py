from flask import Flask
from flask import render_template
from flask import request
import boto3

from flask import Flask, redirect, url_for, request
app = Flask(__name__)
instance_is_on = True

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

@app.route('/')
def index():
    users = [ 'Rosalia','Adrianna','Victoria','Mihad','Angelina' ]
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
   return render_template('instances.html', title='EC2 Instances', instances=obj)

def turnOnOffInstance(instanceId):
   if instance_is_on == True:
      ec2_resource = boto3.client('ec2')
      response = ec2_resource.stop_instances(
      InstanceIds=[
         [instanceId],
      ]
      )
      return
   ec2_resource = boto3.client('ec2')
   response = ec2_resource.start_instances(
   InstanceIds=[
      [instanceId],
   ]

   

app.run(host='0.0.0.0', port=81)
