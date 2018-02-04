import boto3
from describe_instances import get_instances
from Stop_Instances import stop_instances

instanceid =  get_instances()
print instanceid
for i in instanceid:
    stop_instances(i)
