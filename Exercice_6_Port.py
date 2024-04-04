import requests
import json

# Define the Port API endpoint URLs
frameworkAPI = "https://api.getport.io/v1/blueprints/githubPullRequest/entities"
blueprintsAPI = "https://api.getport.io/v1/blueprints"
Token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdJZCI6Im9yZ19RcGUxak90cGZBZ0RFZzBKIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2V0cG9ydC5pbyIsImlzTWFjaGluZSI6dHJ1ZSwic3ViIjoiVmNMVHNkNzE3R0piNXprZGpRUFg4YzlJSEZxSTVHS3UiLCJqdGkiOiJmOGUxM2JhMi03NTY0LTRmNmItOWU4NS0yMTJlZTE5NTJlOTEiLCJpYXQiOjE3MTIyMTg1NjAsImV4cCI6MTcxMjIyOTM2MH0.IrL1oJdzBE6g6vZSd0BqoiRL1iR84lAI6zX-D1u8HeY"


'''
response = requests.get(frameworkAPI, headers={"Authorization": Token}).json()
for entity in response['entities']:
    entitiesAPI = frameworkAPI + '/' + entity['identifier']
    entity['properties']['State'] = 'EOL'
    entity['icon'] = ''
    entity['properties']['closedAt'] = '2024-04-02T07:16:03.487Z'
    entity['properties']['mergedAt'] = '2024-04-02T07:15:30.487Z'

    requests.post(frameworkAPI, params=json.dumps(entity), headers={"Authorization": Token})
'''


#---------------------- just count the EOL
response = requests.get(blueprintsAPI, headers={"Authorization": Token}).json()

blueprints = []
for blueprint in response['blueprints']:
    blueprints.append(blueprint['identifier'])

counter = 0
for element in blueprints:
    entitiesAPI = "https://api.getport.io/v1/blueprints/" + element + "/entities"
    response = requests.get(entitiesAPI, headers={"Authorization": Token}).json()

    for entity in response['entities']:
        try:
            if entity['properties']['State'] == 'EOL':
                counter += 1
        except:
            continue

print(counter)

#---------------------- just count the EOL

