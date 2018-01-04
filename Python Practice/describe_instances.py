import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
filters = [{ 'Name': 'tag:Name','Values': [ 'balakrihna' ] }]
response = ec2.describe_instances(Filters = filters)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        #print(instance)
        print(instance["InstanceId"])

