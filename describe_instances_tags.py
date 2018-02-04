import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def get_tags():
    filters = [{ 'Name':'tag:Owner','Values':[ 'balakrishna' ] }]
    response = ec2.describe_instances(Filters = filters)
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            for key in instance["Tags"]:
                if  key['Key']== 'date':
                    return key['Value']


print(get_tags())
