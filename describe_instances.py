import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
mylist = []
def get_instances():
    filters = [{ 'Name': 'tag:Owner','Values': [ sys.argv[1]] }]
    response = ec2.describe_instances(Filters = filters)
    #print response
    for reservation in response["Reservations"]:
        for instnace in reservation["Instances"]:
            print instnace["State"]["Name"]
    #return mylist


get_instances()
