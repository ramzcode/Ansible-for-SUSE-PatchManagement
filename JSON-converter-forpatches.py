import json

# Read the data from the file
with open('data.txt', 'r') as file:
    data = file.read()

# Split the data into lines
lines = data.split('\n')

# Initialize a dictionary to store the patch information
patch_info = {}

# Process each line and extract key-value pairs
for line in lines:
    # Skip empty lines or lines without a colon separator
    if not line.strip() or ':' not in line:
        continue

    # Split the line into key and value
    key, value = line.split(':', 1)

    # Remove leading/trailing whitespace from the key and value
    key = key.strip()
    value = value.strip()

    # Check if the key is "Conflicts"
    if key == "Conflicts":
        # Initialize an empty array to store the conflicts
        conflicts = []

        # Process each line under the "Conflicts" block
        while True:
            # Read the next line
            line = lines.pop(0)

            # Check if the line starts with whitespace or contains a colon
            if line.startswith(' ') or ':' in line:
                # Remove the leading whitespace and add the line to the conflicts array
                conflicts.append(line.strip())
            else:
                # Put the last read line back to the lines list
                lines.insert(0, line)
                break

        # Add the conflicts array to the patch_info dictionary
        patch_info[key] = conflicts
    else:
        # Add the key-value pair to the patch_info dictionary
        patch_info[key] = value

# Convert the patch_info dictionary to JSON
json_data = json.dumps(patch_info, indent=4)

# Print the JSON data
print(json_data)

