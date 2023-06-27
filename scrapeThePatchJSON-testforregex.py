import json
import re

# Specify the path to the JSON file
json_file_path = "file.json"

# Read the JSON data from the file
with open(json_file_path, "r") as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Define the regex pattern to search for
pattern = r"glibc.* < 2.31-150300.46.1"

# Iterate through the data to find the matching entry
for entry in data:
    conflicts = entry.get("Conflicts", [])
    for conflict in conflicts:
        if re.search(pattern, conflict):
            severity = entry.get("Severity")
            category = entry.get("Category")
            print("Severity:", severity)
            print("Category:", category)
            #print("Matching conflict:", conflict)
            break  # Exit the loop after finding the matching entry
    else:
        continue
    break  # Exit the outer loop after finding the matching entry

