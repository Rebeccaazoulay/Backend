# Mock data for demonstration
service_entities = [
    {"name": "Service A", "used_frameworks": ["Framework 1", "Framework 2"]},
    {"name": "Service B", "used_frameworks": ["Framework 2", "Framework 3"]},
    # Add more service entities as needed
]

framework_entities = [
    {"name": "Framework 1", "state": "Active"},
    {"name": "Framework 2", "state": "EOL"},
    {"name": "Framework 3", "state": "Active"},
    # Add more framework entities as needed
]

# Function to update the Number of EOL packages property for each service entity
def update_eol_packages(service_entities, framework_entities):
    for service in service_entities:
        eol_packages_count = 0
        for framework_name in service["used_frameworks"]:
            # Find the framework entity
            framework = next((fw for fw in framework_entities if fw["name"] == framework_name), None)
            if framework and framework["state"] == "EOL":
                eol_packages_count += 1
        service["number_of_eol_packages"] = eol_packages_count

# Call the function to update the Number of EOL packages property
update_eol_packages(service_entities, framework_entities)

# Display the updated service entities
for service in service_entities:
    print(f"Service: {service['name']}, Number of EOL packages: {service.get('number_of_eol_packages', 0)}")
