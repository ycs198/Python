import boto3
import time

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
        for vpc in response['Vpcs']:
            return vpc['VpcId']

    def get_route_table(self):
        response2 = self.ec2.describe_route_tables()
        for routetable in response2['RouteTables']:
            for id in routetable['Associations']:
                return id['RouteTableId']

    def create_subnets(self,cidr_blcok,vpcid,zone):
        self.zone = zone
        self.cidr_block = cidr_blcok
        response = self.ec2.create_subnet(AvailabilityZone=zone,CidrBlock=cidr_blcok,VpcId=vpcid)
        return response['Subnet']['SubnetId']


    def create_internet_gateway(self,vpc):
        self.vpc = vpc
        response =  self.ec2.create_internet_gateway()
        internet_id = response['InternetGateway']['InternetGatewayId']
        response2 = self.ec2.attach_internet_gateway(InternetGatewayId=internet_id,VpcId=vpc)
        print "attaching the intergatway {}  to the vpc:{}".format(internet_id,vpc)
        return internet_id

    def allocate_elastic_address(self):
        response = self.ec2.allocate_address(Domain='vpc')
        return response['AllocationId']

    def public_route_table(self,vpc):
        self.vpc = vpc
        response = self.ec2.create_route_table(VpcId=vpc)
        return response['RouteTable']['RouteTableId']


    def create_Tags(self,tag_dict,vpc):
        return self.ec2.create_tags(Resources=[vpc],Tags=tag_dict)

    def update_route_table(self,destination,internet_id,routetableid):
        updated = self.ec2.create_route(DestinationCidrBlock=destination,GatewayId=internet_id,RouteTableId=routetableid)
        return updated

    def associcate_route_table(self,route_table_id,subnet_id):
        response = self.ec2.associate_route_table(RouteTableId=route_table_id,SubnetId=subnet_id)
        return response

    def create_nat_gateway(self,elastic_ip_id,subnet_id):
        response = self.ec2.create_nat_gateway(AllocationId=elastic_ip_id,SubnetId=subnet_id)
        return response['NatGateway']['NatGatewayId']


bala = Create_Vpc('us-east-1','10.0.0.0/16')
bala.create_vpc()
vpc= bala.describe_vpc()
elastic_ip = bala.allocate_elastic_address()
print elastic_ip
def_rt_table_id = bala.get_route_table()
route_table_tag_private = [{'Key':'Name','Value':'RouteTable-private'}]
print bala.create_Tags(route_table_tag_private,def_rt_table_id)
vpc_tag = [{ 'Key':'Name','Value' : 'Freelancing'}]
print bala.create_Tags(vpc_tag,vpc)
Public_subnet=bala.create_subnets('10.0.0.0/24',vpc,'us-east-1d')
print Public_subnet
Public_sub_tag = [{'Key':'Name','Value':'Public-subnet' }]
print bala.create_Tags(Public_sub_tag,Public_subnet)
Private_subnet=bala.create_subnets('10.0.1.0/24',vpc,'us-east-1c')
Private_sub_tag = [{'Key':'Name','Value':'Public-subnet' }]
print bala.create_Tags(Private_sub_tag,Private_subnet)
ig_id= bala.create_internet_gateway(vpc)
internet_tag = [{'Key':'Name','Value':'Intergateway-public'}]
bala.create_Tags(internet_tag,ig_id)
rt_id =bala.public_route_table(vpc)
print rt_id
route_table_tag = [{'Key':'Name','Value':'RouteTable-public'}]
print bala.create_Tags(route_table_tag,rt_id)
print bala.update_route_table('0.0.0.0/0',ig_id,rt_id)
print bala.associcate_route_table(def_rt_table_id,Private_subnet)
print bala.associcate_route_table(rt_id,Public_subnet)
nat_id = bala.create_nat_gateway(elastic_ip,Public_subnet)
print nat_id
nat_tag = [{'Key':'Name','Value':'natgateway-public'}]
bala.create_Tags(nat_tag,nat_id)
time.sleep(60)
print bala.update_route_table('0.0.0.0/0',nat_id,def_rt_table_id)
