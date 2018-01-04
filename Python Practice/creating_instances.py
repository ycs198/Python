import boto3
#from botocore.execptions import ClientError

ec2 = boto3.resource('ec2')
def creating_instances(amiid,min,max,type):
    instance = ec2.create_instances(ImageId = 'amiid',MinCount=min,MaxCount=max,InstanceType='type')
    return instance[0].id

