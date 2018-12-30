import requests

payload = {'_format:json','access-token:ggolvSv4UpUH_a9Qk5x5KAC2YudbptpltVYZ'}
response = requests.get('https://gorest.co.in/public-api/users?_format=json&access-token=ggolvSv4UpUH_a9Qk5x5KAC2YudbptpltVYZ')
print response.json()
