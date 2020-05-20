
import requests
import json

json_string = 'json'

endpoint = '/api/v1/us/current.{}'.format(json_string)
website = 'https://covidtracking.com'

url = website + endpoint  

res = requests.get(url)

print(res.headers) # returns the headers of the response
print(res.json()) # returns the dataset