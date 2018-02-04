import boto3
from botocore.exceptions import  ClientError
from flask import Flask,render_template
from describe_instances import get_instances

ec2 = boto3.client('ec2')

app = Flask(__name__)

@app.route('/')
def instances():
    return str(get_instances())

app.run()
