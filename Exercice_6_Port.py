import requests
import json

# Define the Port API endpoint URLs
BLUEPRINTS_ENDPOINT = "https://api.getport.io/v1/blueprints"
frameworkAPI = "https://api.getport.io/v1/blueprints/githubPullRequest/entities"
blueprintsAPI = "https://api.getport.io/v1/blueprints"
post_blueprintsAPI = "https://api.postport.io/v1/blueprints"
Get_API = "https://api.getport.io/static/index.html#/Entities/get_v1_blueprints__blueprint_identifier__entities"
Token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdJZCI6Im9yZ19RcGUxak90cGZBZ0RFZzBKIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2V0cG9ydC5pbyIsImlzTWFjaGluZSI6dHJ1ZSwic3ViIjoiVmNMVHNkNzE3R0piNXprZGpRUFg4YzlJSEZxSTVHS3UiLCJqdGkiOiJmOGUxM2JhMi03NTY0LTRmNmItOWU4NS0yMTJlZTE5NTJlOTEiLCJpYXQiOjE3MTIyMTg1NjAsImV4cCI6MTcxMjIyOTM2MH0.IrL1oJdzBE6g6vZSd0BqoiRL1iR84lAI6zX-D1u8HeY"

#response = requests.post(frameworkAPI, headers={"Authorization": Token}).json()

#response = requests.get(frameworkAPI, headers={"Authorization": Token}, params={"blueprint_identifier": "framework"}).json()

response = requests.get(frameworkAPI, headers={"Authorization": Token}).json()
for entity in response['entities']:
    entitiesAPI = frameworkAPI + '/' + entity['identifier']
    entity['properties']['State'] = 'EOL'
    entity['icon'] = ''
    entity['properties']['closedAt'] = '2024-04-02T07:16:03.487Z'
    entity['properties']['mergedAt'] = '2024-04-02T07:15:30.487Z'

    requests.post(frameworkAPI, params=json.dumps(entity), headers={"Authorization": Token})


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


#post_response = requests.post(frameworkAPI, headers={"Authorization": Token}).json()

"""
def create_entities():
    # Create service blueprint
    service_blueprint_data = {
        "name": "Service",
        "properties": {
            "Number of EOL packages": {"type": "integer"}
            # Add other properties as needed
        }
    }
    response = requests.post(BLUEPRINTS_ENDPOINT, auth=AUTH, json=service_blueprint_data)
    print("Service Blueprint Creation Response:", response.text)  # Add this line to print response content

    # Check if the response status code is successful
    if response.status_code == 201:  # Corrected status code to check for successful creation
        service_blueprint_id = response.json().get('id')
        print("Service Blueprint ID:", service_blueprint_id)  # Add this line to print the blueprint ID
    else:
        print("Failed to create service blueprint. Status code:", response.status_code)
        return

    # Create framework blueprint
    framework_blueprint_data = {
        "name": "Framework",
        "properties": {
            "State": {"type": "string", "enum": ["Active", "EOL"]}
            # Add other properties as needed
        }
    }
    response = requests.post(BLUEPRINTS_ENDPOINT, auth=AUTH, json=framework_blueprint_data)
    print("Framework Blueprint Creation Response:", response.text)  # Add this line to print response content

    # Check if the response status code is successful
    if response.status_code == 201:  # Corrected status code to check for successful creation
        framework_blueprint_id = response.json().get('id')
        print("Framework Blueprint ID:", framework_blueprint_id)  # Add this line to print the blueprint ID
    else:
        print("Failed to create framework blueprint. Status code:", response.status_code)
        return

    # Now create entities using the blueprints and define the relation between service and framework
    # Use the POST request to create entities


def main():
    create_entities()

if __name__ == "__main__":
    main()
"""

