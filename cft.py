import boto3

def update_cft():
  client = boto3.client('cloudformation')
  with open('/tmp/cft.json',r) as f:
    res = client.update_stack(stackName=cftname,TemplateBody=f.read(),Parameters= [{'ParameterKey':'nameoftheparamete','ParameterValue':'valueoftheparameter'},{'ParameterKey':'nameoftheparamete','ParameterValue':'valueoftheparameter'}])
