import boto3

ec2 = boto3.client('ec2')
filters_apply = [{'Name':'tag:tagname','Values':['tagvalue']}]

def ec2_list():
    res = ec2.describe_instances(Filters=filters_apply)
    return [instance['InstanceId'] for reservation in res['Reservations'] for instance in reservation['Instances']]


def create_tags(resourceid,resourcename):
    client = boto3.client('ec2')
    response = client.create_tags(Resources=[resourceid],Tags=[{'Key': 'lambda','Value': 'CreatedBYBALA'},])
    print("updated the tags: " + resourcename)
    print(response)

def sg_list():
    res = ec2.describe_security_groups(Filters=filters_apply)
    return [sg['GroupId'] for sg in res['SecurityGroups']]

def subnets_list():
    res = ec2.describe_subnets(Filters=filters_apply)
    return [sub['SubnetId']for sub in res['Subnets']]

def vpcs_list():
    res = ec2.describe_vpcs(Filters=filters_apply)
    return [vpc['VpcId']for vpc in res['Vpcs']]

def ebs_volumes_list():
    res = ec2.describe_volumes(Filters=filters_apply)
    return [vol['VolumeId'] for vol in res['Volumes']]

def internet_gateway_list():
    res = ec2.describe_internet_gateways(Filters=filters_apply)
    return [igw['InternetGatewayId']for igw in res['InternetGateways']]

def network_interfaces_list():
    res = ec2.describe_network_interfaces(Filters=filters_apply)
    return [netint['NetworkInterfaceId']for netint in res['NetworkInterfaces']]

def ami_list():
    res = ec2.describe_images(Filters=filters_apply)
    return [ami['ImageId'] for ami in res['Images']]


def main():
    resources_kv = {}
    resources_kv['Ec2Instances'] = ec2_list()
    resources_kv['SecurityGroups'] = sg_list()
    resources_kv['Subnets'] = subnets_list()
    resources_kv['Vpcs'] = vpcs_list()
    resources_kv['EBS'] = ebs_volumes_list()
    resources_kv['InternetGateways'] = internet_gateway_list()
    resources_kv['NetworkInterfaces'] = network_interfaces_list()
    resources_kv['Amis'] = ami_list()
    for k,v in resources_kv.items():
        for i in v:
            print("updating {} of the resource id {}".format(k,i))
            create_tags(i,k)
            
            
if __name__ == '__main__':
    main()
