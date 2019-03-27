import boto3
def lambda_handler():
    ec2 =boto3.client('ec2')
    filters_apply = [{'Name':'tag:OwnerContact','Values':['tagvalue']}]
    res = ec2.describe_instances()
    response = ec2.describe_instances(Filters = filters_apply)
    instance_with_tags = []
    all_instance =[]
    for reservation in res['Reservations']:
        for instance in reservation['Instances']:
            for tag_name in instance['Tags']:
                if tag_name['Key'] == 'Name':
                    all_instance.append(tag_name['Value'])
    
    
    for reservation in response:
        for instance in reservation['Instances']:
            for tag_name in instance['Tags']:
                if tag_name['Key'] == 'Name':
                    instance_with_tags.append(tag_name['Value'])
    
    message = str()
    for i in all_instance:
        if i not in instance_with_tags:
            message = message + 'Name:' + i + '\n'
    
    print message
    client = boto3.client('sns')
    snsresponse = client.publish(TopicArn='topicarn')
    print snsresponse
