import json

data = '''Information for patch SUSE-SLE-Product-SLES-15-SP4-2023-1916:
-------------------------------------------------------------
Repository  : SLE-Product-SLES15-SP4-Updates
Name        : SUSE-SLE-Product-SLES-15-SP4-2023-1916
Version     : 1
Arch        : noarch
Vendor      : maint-coord@suse.de
Status      : needed
Category    : recommended
Severity    : low
Created On  : Wed Apr 19 19:48:02 2023
Interactive : ---
Summary     : Recommended update for sles-release
Description :
    This update for sles-release fixes the following issue:

    - Filter libhogweed4 and libnettle6 so they dont get orphaned on system upgrades. (bsc#1208529)
Provides    : patch:SUSE-SLE-Product-SLES-15-SP4-2023-1916 = 1
Conflicts   : [3]
    sles-release.noarch < 15.4-150400.58.7.3
    sles-release.x86_64 < 15.4-150400.58.7.3'''

# Split the data into lines
lines = data.split('\n')

# Create a dictionary to store the parsed data
parsed_data = {}

# Iterate over the lines and extract key-value pairs
for line in lines:
    if line.strip() != '':
        if ':' in line:
            key, value = line.split(':', 1)
            parsed_data[key.strip()] = value.strip()

# Process the "Conflicts" block
conflicts_lines = []
is_conflicts_block = False

for line in lines:
    if line.strip().startswith('Conflicts'):
        is_conflicts_block = True
        # Remove the brackets from the Conflicts line
        parsed_data['Conflicts'] = line.split(':', 1)[1].strip().strip('[]')
    elif is_conflicts_block and line.startswith('    '):
        conflicts_lines.append(line.strip())

# Add the conflicts lines as an array list
if conflicts_lines:
    parsed_data['Conflicts'] = conflicts_lines

# Convert the dictionary to JSON
json_data = json.dumps(parsed_data, indent=4)

# Print the JSON data
print(json_data)

