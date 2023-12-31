import json

# Specify the path to the JSON file
json_file_path = "file.json"

# Read the JSON data from the file
with open(json_file_path, "r") as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Search for the specific entry
search_entry = "vim-data.noarch < 9.0.1572-150000.5.46.1"

# Iterate through the data to find the matching entry
for entry in data:
    conflicts = entry.get("Conflicts", [])
    if search_entry in conflicts:
        severity = entry.get("Severity")
        category = entry.get("Category")
        print("Severity:", severity)
        print("Category:", category)
        break  # Exit the loop after finding the matching entry

