import boto3
import os
import sys

def get_volume_id(tag_value):
    filters = [{ 'Name': 'tag:aws:cloudformation:stack-name','Values':tag_value}]
    response = ec2.describe_volumes(Filters=filters)
    for volume in response['Volumes']:
        for attachment in volume['Attachments']:
            return attachment['VolumeId']


def create_ebs_snapshot(volumeid):
    snapshot = ec2.create_snapshot(VolumeId=volumeid)
    return snapshot


os.system('export http_proxy= ')
os.system('export https_proxy=')
os.system('export NO_PROXY= ')

name = str(sys.argv[1])
region_name = str(sys.argv[2])
ec2 = boto3.resource('ec2',region=region_name)
print create_ebs_snapshot(get_volume_id(name))['SnapshotId']
