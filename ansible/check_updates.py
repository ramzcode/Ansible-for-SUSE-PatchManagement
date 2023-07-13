import sys
import re
import ast

applied_updates = ast.literal_eval(sys.argv[1])
patch_list = ast.literal_eval(sys.argv[2])

matched_packages = []

for package in patch_list:
    pattern = r"\b{}\b".format(package)
    for update in applied_updates:
        if re.search(pattern, update):
            matched_packages.append(package)
            break

match_count = len(matched_packages)

print("Total_matches:", match_count)
print("Matched_packages:", ", ".join(matched_packages))
