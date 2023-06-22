import json

file_path = 'file.txt'

# Read the contents of the file
with open(file_path, 'r') as file:
    data = file.read()

# Split the data into blocks
blocks = data.split('Information for patch')[1:]

# Create a list to store the parsed data for each block
parsed_blocks = []

# Iterate over the blocks and extract the information
for block in blocks:
    lines = block.split('\n')
    parsed_data = {}
    conflicts_lines = []
    is_conflicts_block = False

    for line in lines:
        if line.strip() != '':
            if ':' in line:
                key, value = line.split(':', 1)
                parsed_data[key.strip()] = value.strip()

            if line.strip().startswith('Conflicts'):
                is_conflicts_block = True
                parsed_data['Conflicts'] = line.split(':', 1)[1].strip().strip('[]')
            elif is_conflicts_block and line.startswith('    '):
                conflicts_lines.append(line.strip())

    if conflicts_lines:
        parsed_data['Conflicts'] = conflicts_lines

    parsed_blocks.append(parsed_data)

# Convert the list of parsed blocks to JSON
json_data = json.dumps(parsed_blocks, indent=4)

# Print the JSON data
print(json_data)

