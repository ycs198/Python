import boto3
from datetime import datetime


ec2 = boto3.client('ec2')

sns = boto3.client('sns')
get_tags_instances = []

def lambda_handler(event, context):
    today_date = get_today_date()
    instance_date = get_tags()
    if today_date == instance_date:
        send_sns()


def get_tags():
    filters = [{ 'Name':'tag:date','Values':[ 'balakrishna' ] }]
    response = ec2.describe_instances(Filters = filters)
    for resveration in response["Reservations"]:
        for instance in resveration["Instnaces"]:
            for key in instance["Tags"]:
                if key['Key'] == 'date':
                    get_tags_instances.append(key['Value'])
            return get_tags_instances

def get_today_date():
    return datetime.today().date()


def send_sns():
    response=sns.publish(TopicArn='arn:aws:sns:us-east-1:385660155691:bala-testing',Message='The instance is 5 days older')
    return response
