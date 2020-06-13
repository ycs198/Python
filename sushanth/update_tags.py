import boto3

def ec2_list():
    res = ec2.describe_instances(Filters=filters_apply)
    return [(instance['InstanceId'],instance['Tags']) for reservation in res['Reservations'] for instance in reservation['Instances']]


def create_tags(resource_meta,resourcename):
    tags_validate = [{'Key': 'lambda','Value': 'CreatedBYBALA'}]
    print(resource_meta[1])
    tags_update = [i for i in tags_validate if i not in resource_meta[1]]
    print(tags_update)
    if len(tags_update) == []:
        print("nothing to update as the tags are existing for the resource" + resource_meta[0])
    else:
        response = ec2.create_tags(Resources=[resource_meta[0]],Tags=tags_update)
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


def get_rds_list():
    filters_apply = [{'Name':'tag:tagname','Values':['tagvalue']}]
    rds = boto3.client('rds')
    res = rds.describe_db_instances(Filters=filters_apply)
    return [(res['DBName'],rds.list_tags_for_resource(ResourceName=res['DBName'])['TagList']) for rds in res['DBInstances']]


def add_rds_tags(dbmetadata):
    rds = boto3.client('rds')
    tags_validate = [{'Key': 'lambda','Value': 'CreatedBYBALA'}]
    tags_update = [i for i in tags_validate if i not in dbmetadata[1]]
    if len(tags_update) == []:
         print("nothing to update as the tags are existing for the resource" + dbmetadata[0])
    else:
        response = rds.add_tags_to_resource(ResourceName=dbmetadata[0],Tags=tags_update)
        print("updated the tags: " + dbmetadata[0])
        print(response)


def get_s3_buckets_list():
    s3 = boto3.client('s3')
    res = s3.list_buckets()
    return [(i['Name'],s3.get_bucket_tagging(Bucket=i['Name'])['TagSet']) for i in res['Buckets']]


def add_s3_tags(bucketmetadata):
    tags_validate = [{'Key': 'lambda','Value': 'CreatedBYBALA'}]
    tags_update = [i for i in tags_validate if i not in bucketmetadata[1]]
    if len(tags_update) == []:
        print("nothing to update as the tags are existing for the resource" + bucketmetadata[0])
    else:
        s3 = boto3.client('s3')
        res = s3.put_bucket_tagging(Bucket=bucketmetadata[0],Tagging={'Tagset':tags_update})
        print(res)

def get_elb_list():
    elb = boto3.client('elb')
    elb_tags_list = []
    res = elb.describe_load_balancers()
    for elbname in res['LoadBalancerDescriptions']:
        name = elbname['LoadBalancerName']
        r = elb.describe_tags(LoadBalancerNames=name)
        elb_tags_list.append((name,r['TagDescriptions'][0]['Tags']))
    return elb_tags_list

def add_elb_tags(elbmetadata):
    tags_validate = [{'Key': 'lambda','Value': 'CreatedBYBALA'}]
    tags_update = [i for i in tags_validate if i not in elbmetadata[1]]
    if len(tags_update) == []:
        print("nothing to update as the tags are existing for the resource" + elbmetadata[0])
    else:
        elb = boto3.client('elb')
        res = elb.add_tags(LoadBalancerNames=[elbmetadata[0]],Tags=tags_update)
        print(res)

def get_asg_list():
    asg = boto3.client('autoscaling')
    asg_tags_list = []
    res = asg.describe_auto_scaling_groups(MaxRecords=100)
    for i in res['AutoScalingGroups']:
        name = i['AutoScalingGroupName']
        filters_apply =  [{'Key': 'tag:Name','Value': name}]
        tags = asg.describe_tags(Filters=filters_apply)['Tags']
        asg_tags_list.append((name,tags))
    return asg_tags_list

#*** for lamdba
#def lambda_handler(event, context):
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    filters_apply = [{'Name':'tag:tagname','Values':['tagvalue']}]
    resources_kv = {}
    resources_kv['Ec2Instances'] = ec2_list()
    resources_kv['SecurityGroups'] = sg_list()
    resources_kv['Subnets'] = subnets_list()
    resources_kv['Vpcs'] = vpcs_list()
    resources_kv['EBS'] = ebs_volumes_list()
    resources_kv['InternetGateways'] = internet_gateway_list()
    resources_kv['NetworkInterfaces'] = network_interfaces_list()
    resources_kv['Amis'] = ami_list()
    resources_kv['S3Bucket'] = get_s3_buckets_list()
    resources_kv['rds'] = get_rds_list()
    resources_kv['elb'] = get_elb_list()
    for k,v in resources_kv.items():
        if k == 'S3Bucket':
            for i in v:
                print("updating {} of the resource id {}".format(k,i[0]))
                add_s3_tags(i)
        elif k == 'rds':
            for i in v:
                print("updating {} of the resource id {}".format(k,i[0]))
                add_rds_tags(i)
        elif k == 'elb':
            for i in v:
                print("updating {} of the resource id {}".format(k,i[0]))
                add_elb_tags(i)
        else:
            for i in v:
                print("updating {} of the resource id {}".format(k,i[0]))
                create_tags(i,k)
