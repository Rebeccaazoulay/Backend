import requests
import json


# Define the Port API endpoint URLs
frameworkAPI = "https://api.getport.io/v1/blueprints/service/entities/Mamat_HW?create_missing_related_entities=false"
blueprintsAPI = "https://api.getport.io/v1/blueprints"
entitiesAPI = "https://api.getport.io/v1/blueprints/service/entities"
Token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdJZCI6Im9yZ19RcGUxak90cGZBZ0RFZzBKIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2V0cG9ydC5pbyIsImlzTWFjaGluZSI6dHJ1ZSwic3ViIjoiVmNMVHNkNzE3R0piNXprZGpRUFg4YzlJSEZxSTVHS3UiLCJqdGkiOiIyMWY4NmZiMi01OWU1LTQyNGYtODhiYi0wMzdjYmVkMDA0NzQiLCJpYXQiOjE3MTIzMDg4NjEsImV4cCI6MTcxMjMxOTY2MX0.mWIC3t_i78SIiEk5GNC8LmEHu1V7U44qyr3I5SkVHaw"


#---------------------- just count the EOL

counter = 0
entitiesAPI = "https://api.getport.io/v1/blueprints/service/entities"
response = requests.get(entitiesAPI, headers={"Authorization": Token}).json()

print(response)

for entity in response['entities']:
    try:
        if entity['properties']['state'] == 'EOL':
            counter += 1
    except:
        continue

#---------------------- just count the EOL

print(counter)

response = requests.get(entitiesAPI, headers={"Authorization": Token}).json()
for entity in response['entities']:
    entity['properties']['number_of_eol_packages'] = counter
    entity['icon'] = ''
    entity['properties']['readme'] = ''
    del(entity['blueprint'], entity['createdAt'], entity['createdBy'], entity['updatedAt'], entity['updatedBy'], entity['scorecards'], entity['scorecardsStats'])
    entity['properties']['closedAt'] = '2024-04-02T07:16:03.487Z'
    entity['properties']['mergedAt'] = '2024-04-02T07:15:30.487Z'
    frameworkAPI = "https://api.getport.io/v1/blueprints/service/entities/" + entity['identifier'] + "?create_missing_related_entities=false"
    post_response = requests.patch(url=frameworkAPI, json=entity, headers={"Authorization": Token}).json()


print(post_response)

