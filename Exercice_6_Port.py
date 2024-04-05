import requests

# Define the Port API endpoint URLs
entitiesAPI = "https://api.getport.io/v1/blueprints/service/entities"
Token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJvcmdJZCI6Im9yZ19RcGUxak90cGZBZ0RFZzBKIiwiaXNzIjoiaHR0cHM6Ly9hcGkuZ2V0cG9ydC5pbyIsImlzTWFjaGluZSI6dHJ1ZSwic3ViIjoiVmNMVHNkNzE3R0piNXprZGpRUFg4YzlJSEZxSTVHS3UiLCJqdGkiOiI2YWZmMmY0NS1iNWQ4LTRjNGYtYjhkOS03NWIwMTY0ZDMzNzAiLCJpYXQiOjE3MTIzMTg5NDAsImV4cCI6MTcxMjMyOTc0MH0.oy2XhdeOmlbYc0tjZbeX69ASb3l07fgGkwl9bR6VEas"


# Function to fetch entities from Port API
def fetch_entities():
    response = requests.get(entitiesAPI, headers={"Authorization": Token}).json()
    return response.get('entities', [])


# Function to count EOL packages among entities
def count_eol_packages(entities):
    counter = 0
    for entity in entities:
        if entity.get('properties', {}).get('state') == 'EOL':
            counter += 1
    return counter


# Function to update entities with EOL package count
def update_entities(entities, counter):
    for entity in entities:
        # Update entity properties
        entity['properties']['number_of_eol_packages'] = counter
        entity['icon'] = ''
        entity['properties']['readme'] = ''
        # Remove unnecessary fields
        del entity['blueprint'], entity['createdAt'], entity['createdBy'], entity['updatedAt'], entity['updatedBy'], \
        entity['scorecards'], entity['scorecardsStats']
        # Set timestamps
        entity['properties']['closedAt'] = '2024-04-02T07:16:03.487Z'
        entity['properties']['mergedAt'] = '2024-04-02T07:15:30.487Z'
        # Prepare API endpoint for entity update
        frameworkAPI = f"https://api.getport.io/v1/blueprints/service/entities/{entity['identifier']}?create_missing_related_entities=false"
        # Send PATCH request to update entity
        requests.patch(url=frameworkAPI, json=entity, headers={"Authorization": Token}).json()


# Main function to orchestrate the update process
def main():
    # Fetch entities from Port API
    entities = fetch_entities()
    # Count EOL packages among entities
    eol_counter = count_eol_packages(entities)
    update_entities(entities, eol_counter)

if __name__ == "__main__":
    main()

