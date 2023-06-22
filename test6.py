import xmltodict
import json

xml_data = '''<?xml version='1.0'?>
<stream>
<message type="info">Refreshing service 'Basesystem_Module_15_SP4_x86_64'.</message>
<message type="info">Refreshing service 'SUSE_Linux_Enterprise_Server_15_SP4_x86_64'.</message>
<message type="info">Refreshing service 'SUSE_Package_Hub_15_SP4_x86_64'.</message>
<message type="info">Refreshing service 'Server_Applications_Module_15_SP4_x86_64'.</message>
<message type="info">Loading repository data...</message>
<message type="info">Reading installed packages...</message>
<message type="info">
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
    srcpackage:sles-release &lt; 15.4-150400.58.7.3
    sles-release.noarch &lt; 15.4-150400.58.7.3
    sles-release.x86_64 &lt; 15.4-150400.58.7.3
</message>
</stream>'''

# Convert XML to OrderedDict
data_dict = xmltodict.parse(xml_data)

# Convert OrderedDict to JSON
json_data = json.dumps(data_dict, indent=4)

# Print the JSON data
print(json_data)

