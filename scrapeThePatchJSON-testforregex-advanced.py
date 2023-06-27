import csv
import json
import re
import sys

# Check if the pattern arguments are provided
if len(sys.argv) < 3:
    print("Usage: python script.py pattern_start pattern_end")
    sys.exit(1)

# Retrieve the command-line arguments
pattern_start = sys.argv[1]
pattern_end = sys.argv[2]

# Specify the path to the JSON file
json_file_path = "file.json"

# Read the JSON data from the file
with open(json_file_path, "r") as file:
    json_data = file.read()

# Parse the JSON data
data = json.loads(json_data)

# Specify the path to the CSV file
csv_file_path = "output.csv"

# Open the CSV file for writing
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Write the CSV header
    writer.writerow(["Update", "Severity", "Category"])

    # Iterate through the data to find the matching entry and write it to the CSV file
    for entry in data:
        conflicts = entry.get("Conflicts", [])
        for conflict in conflicts:
            if re.search(f"{re.escape(pattern_start)}.* < {re.escape(pattern_end)}", conflict):
                severity = entry.get("Severity")
                category = entry.get("Category")
                writer.writerow([pattern_start, severity, category])
                break  # Exit the loop after finding the matching entry
        else:
            continue
        break  # Exit the outer loop after finding the matching entry

