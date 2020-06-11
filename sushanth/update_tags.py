import boto3

ec2 = boto3.client('ec2')
filters_apply = [{'Name':'tag:tagname','Values':['tagvalue']}]

def ec2_list():
    res = ec2.describe_instances(Filters=filters_apply)
    return [(instance['InstanceId'],instance['Tags']) for reservation in res['Reservations'] for instance in reservation['Instances']]


def create_tags(resource_meta,resourcename):
    tags_validate = [{'Key': 'lambda','Value': 'CreatedBYBALA'}]
    tags_update = [i for i in tags_validate if i not in resource_meta[1]]        
    response = ec2.create_tags(Resources=[resource_meta[0]],Tags=[tags_update])
    print("updated the tags: " + resourcename)
    print(response)

def sg_list():
    res = ec2.describe_security_groups(Filters=filters_apply)
    return [(sg['GroupId'],sg['Tags']) for sg in res['SecurityGroups']]

def subnets_list():
    res = ec2.describe_subnets(Filters=filters_apply)
    return [(sub['SubnetId'],sub['Tags'])for sub in res['Subnets']]

def vpcs_list():
    res = ec2.describe_vpcs(Filters=filters_apply)
    return [(vpc['VpcId'],vpc['Tags'])for vpc in res['Vpcs']]

def ebs_volumes_list():
    res = ec2.describe_volumes(Filters=filters_apply)
    return [(vol['VolumeId'],vol['Tags']) for vol in res['Volumes']]

def internet_gateway_list():
    res = ec2.describe_internet_gateways(Filters=filters_apply)
    return [(igw['InternetGatewayId'],igw['Tags'])for igw in res['InternetGateways']]

def network_interfaces_list():
    res = ec2.describe_network_interfaces(Filters=filters_apply)
    return [(netint['NetworkInterfaceId'],netint['TagSet'])for netint in res['NetworkInterfaces']]

def ami_list():
    res = ec2.describe_images(Filters=filters_apply)
    return [(ami['ImageId'],ami['Tags']) for ami in res['Images']]


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
            print("updating {} of the resource id {}".format(k,i[0]))
            create_tags(i,k)



if __name__ == '__main__':
    main()
