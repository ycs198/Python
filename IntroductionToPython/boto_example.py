from flask import Flask
import boto3

#app = Flask(__name__)

#@app.route('/')
def example(instnacename):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)


#app.run()

