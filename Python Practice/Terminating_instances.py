import sys
import datetime
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def get_instance():
    response = ec2.describe_instances(Filters = [ { 'Name' : 'tag:Name','Values': [ 'balakrihna2' ]}])
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            return instance["InstanceId"]


def terminating_instance(instance_id):
    try:
        ec2.terminate_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id],DryRun=False)
        print(response)
    except:
        print(e)

instanceid = get_instance()
print (instanceid)

terminating_instance(instanceid)
