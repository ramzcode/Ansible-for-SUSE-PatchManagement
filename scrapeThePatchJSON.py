import json

# Specify the path to the JSON file
json_file_path = "file.json"

# Read the JSON data from the file
with open(json_file_path, "r") as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Search for the specific entry
search_entry = "python3-firewall < 0.9.3-150400.8.3.19"

# Iterate through the data to find the matching entry
for entry in data:
    conflicts = entry.get("Conflicts", [])
    if search_entry in conflicts:
        severity = entry.get("Severity")
        category = entry.get("Category")
        print("Severity:", severity)
        print("Category:", category)
        break  # Exit the loop after finding the matching entry

