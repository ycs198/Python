import sys
import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
def stop_instances(instanceid):
	try:
		ec2.stop_instances(InstanceIds=[instanceid], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			raise
	try:
		response =ec2.stop_instances(InstanceIds=[instanceid],DryRun=False)
		print(response)
	except:
		print(e)
