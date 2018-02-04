import boto3
#from botocore.execptions import ClientError

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(ImageId = 'ami-26ebbc5c',MinCount=1,MaxCount=2,InstanceType='t2.micro')
print instance[0].id




