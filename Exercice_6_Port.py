import requests
import json


# Define the Port API endpoint URLs
frameworkAPI = "https://api.getport.io/v1/blueprints/service/entities"
blueprintsAPI = "https://api.getport.io/v1/blueprints"
entitiesAPI = "https://api.getport.io/v1/blueprints/service/entities"
Token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdJZCI6Im9yZ19RcGUxak90cGZBZ0RFZzBKIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2V0cG9ydC5pbyIsImlzTWFjaGluZSI6dHJ1ZSwic3ViIjoiVmNMVHNkNzE3R0piNXprZGpRUFg4YzlJSEZxSTVHS3UiLCJqdGkiOiI3ZmZjZGQwYi05NTIyLTRhNTItOWYyYS02YTY0Y2M1YTNiOWQiLCJpYXQiOjE3MTIyMjgzNDEsImV4cCI6MTcxMjIzOTE0MX0.qX2wCD11LzK3pCQu6fOFEvQdhsg0SPJqs7qziKV1ukc"


#---------------------- just count the EOL

counter = 0
entitiesAPI = "https://api.getport.io/v1/blueprints/service/entities"
response = requests.get(entitiesAPI, headers={"Authorization": Token}).json()

for entity in response['entities']:
    try:
        if entity['properties']['state'] == 'EOL':
            counter += 1
    except:
        continue

#---------------------- just count the EOL

response = requests.get(frameworkAPI, headers={"Authorization": Token}).json()
for entity in response['entities']:
    entity['properties']['number_of_eol_packages'] = counter
    post_response = requests.post(frameworkAPI, data=json.dumps(entity), headers={"Authorization": Token}).json()



