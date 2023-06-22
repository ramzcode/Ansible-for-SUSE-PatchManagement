import json

data = '''
Information for patch SUSE-SLE-Product-SLES-15-SP4-2023-1916:
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
    sles-release.x86_64 < 15.4-150400.58.7.3

Information for patch SUSE-SLE-Product-SLES-15-SP4-2023-1917:
-------------------------------------------------------------
Repository  : SLE-Product-SLES15-SP4-Updates
Name        : SUSE-SLE-Product-SLES-15-SP4-2023-1917
Version     : 1
Arch        : noarch
Vendor      : maint-coord@suse.de
Status      : needed
Category    : recommended
Severity    : low
Created On  : Wed Apr 20 10:15:20 2023
Interactive : ---
Summary     : Recommended update for kernel-firmware
Description :
    This update for kernel-firmware fixes the following issues:
    - Update to version 20230207 (git changelog):
      * Mellanox: Add new mlxsw_spectrum firmware 13.2000.00
      * AMD: Add new Navi14 firmware images
Provides    : patch:SUSE-SLE-Product-SLES-15-SP4-2023-1917 = 1
Conflicts   : [2]
    srcpackage:kernel-firmware < 20230207-4.6.3
    kernel-firmware < 20230207-4.6.3
'''

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

