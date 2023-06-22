import json

# Load the original JSON data
with open('data.json') as file:
    data = json.load(file)

# Create a new dictionary with embedded objects under "name" value
updated_data = {
    'version': data['version'],
    'update_list': {
        'update': []
    }
}

for item in data['update_list']['update']:
    name_value = item.pop('name')
    item = {name_value: item}
    updated_data['update_list']['update'].append(item)

# Save the updated JSON data to a file
with open('updated_data.json', 'w') as file:
    json.dump(updated_data, file, indent=4)

