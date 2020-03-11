import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError


##To GET the  Cloudwatch Get for particular instance id 
def cloudwatch_data(instanceid):
    client = boto3.client('cloudwatch')
    res = client.get_metric_statistics(Namespace="AWS/EC2",MetricName="CPUUtilization",Period=300,Statistics=['Average'],Dimensions=[{'Name': 'InstanceId','Value': 'instanceid'}],StartTime=datetime.utcnow() - timedelta(minutes=15),EndTime=datetime.utcnow())
    datapoints_lists = [i['Average'] for i in res['Datapoints']]
    #print(datapoints_lists)
    if datapoints_lists[0] < 10 and datapoints_lists[1] < 10 and datapoints_lists[2] < 10:
        print("stopping instace")
        #Stoping the instnace if the cpuutilization is less than 10 for 3 consecutive data points 
        stop_instanes(instanceid)
    else:
        print("removing tags")
        #removing the monitor tag from the instnace as it is not needed
        remove_tags(instanceid)

#function To Stop the instnaces
def stop_instanes(instanceid):
    ec2 = boto3.client('ec2')
    try:
        ec2.stop_instances(InstanceIds=[instanceid], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    try:
        response = ec2.stop_instances(InstanceIds=[instanceid], DryRun=False)
        print(response)
    except:
        print(e)
        
#function to Remove the montior tag from the instance
def remove_tags(instanceid):
    ec2 = boto3.resource('ec2')
    tag = ec2.Tag(instanceid, 'Monitor', 'True')
    tag.delete(DryRun=False)

#function To get the list of the instancesid with the monitor tag
def get_instanceid():
    ec2 = boto3.client('EC2')
    response = ec2.describe_instances(Filters=[{'Name': 'tag:Monitor', 'Values': ['True']}])
    return [instance["InstanceId"] for reservation in response["Reservations"] for instance in reservation["Instances"]]


#lambda Main function
def lamdba_handler(event,context):
    for i in get_instanceid():
        cloudwatch_data(i)
