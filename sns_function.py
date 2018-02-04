import boto3
from botocore.utils import ClientError

sns = boto3.client('sns')
def send_sns():
    response = sns.publish(TopicArn='arn:aws:sns:us-east-1:385660155691:bala-testing',Message='The instance is 5 days older')
    print response

send_sns()
