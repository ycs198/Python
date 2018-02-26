import boto3
class Create_Vpc:
    def __init__(self,region,cidr_block):
        self.cidr_block = cidr_block
        self.region = region
        self.ec2 = boto3.client('ec2',region_name=self.region)

    def create_vpc(self):
        response = self.ec2.create_vpc(CidrBlock=self.cidr_block,AmazonProvidedIpv6CidrBlock=False,InstanceTenancy='default')
        return response

    def describe_vpc(self):
        response = self.ec2.describe_vpcs()
        print response
        response2 = self.ec2.describe_route_tables()
        for routetable in response2['RouteTables']:
            for id in routetable['Associations']:
                print id['RouteTableId']
        for vpc in response['Vpcs']:
            return vpc['VpcId']

    def create_subnets(self,cidr_blcok,vpcid,zone):
        self.zone = zone
        self.cidr_block = cidr_blcok
        response = self.ec2.create_subnet(AvailabilityZone=zone,CidrBlock=cidr_blcok,VpcId=vpcid)
        return response


    def create_internet_gateway(self,vpc):
        self.vpc = vpc
        response =  self.ec2.create_internet_gateway()
        internet_id = response['InternetGateway']['InternetGatewayId']
        response2 = self.ec2.attach_internet_gateway(InternetGatewayId=internet_id,VpcId=vpc)
        print "attaching the intergatway {}  to the vpc:{}".format(internet_id,vpc)
        return internet_id

    def allocate_elastic_address(self):
        response = self.ec2.allocate_address(Domain='vpc')
        return response

    def public_route_table(self,vpc):
        self.vpc = vpc
        response = self.ec2.create_route_table(VpcId=vpc)
        for routetable in response['RouteTables']:
            for id in routetable['Associations']:
                return id['RouteTableId']


    def create_Tags(self,tag_dict,vpc):
        return self.ec2.create_tags(Resources=[vpc],Tags=tag_dict)

bala = Create_Vpc('us-east-1','10.0.0.0/16')
bala.create_vpc()
vpc= bala.describe_vpc()
vpc_tag = [{ 'Key':'Name','Value' : 'Freelancing'}]
bala.create_Tags(vpc_tag,vpc)

#bala.create_subnets('10.0.0.0/24',vpc,'us-east-1d')
#bala.create_subnets('10.0.1.0/24',vpc,'us-east-1c')
id = bala.create_internet_gateway(vpc)
print id
internet_tag = [{'Key':'Name','Value':'Intergateway-public'}]
bala.create_Tags(internet_tag,id)
