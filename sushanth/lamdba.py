import boto3


def create_tags(resourceid,resourcename):
    client = boto3.client('ec2')
    response = client.create_tags(Resources=[resourceid],Tags=[{'Key': 'lambda','Value': 'CreatedBYBALA'},])
    print("updated the tags: " + resourcename)
    print(response)

def get_vpc_id(event):
    id = event['detail']['responseElements']['vpc']['vpcId']
    return id

def get_subnet_id(event):
    id = event['detail']['responseElements']['subnet'] ['subnetId']
    return id

def get_internetgateway_id(event):
    id = event['detail']['responseElements']['internetGateway']['internetGatewayId']
    return id

def get_securitygroup_id(event):
    id = event['detail']['responseElements']['groupId']
    return id

def lambda_handler(event, context):
    if event['detail']['eventName'] == 'CreateInternetGateway':
        id = get_internetgateway_id(event)
        create_tags(id,"internetGateway")
    elif event['detail']['eventName'] == 'CreateVpc':
        id = get_vpc_id(event)
        create_tags(id,"VPC")
    elif event['detail']['eventName'] == 'CreateSubnet':
        id = get_subnet_id(event)
        create_tags(id,"Subnet")
    elif event['detail']['eventName'] == 'CreateSecurityGroup':
        id = get_securitygroup_id(event)
        create_tags(id,"SecurityGroup")
