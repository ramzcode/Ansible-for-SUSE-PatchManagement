# SUSE
## How it works
1. Scan for Updates
2. Scan for Patches
3. zypper outputs in xml using -x format for zypper -x lu & lp
4. convert the xml to JSON from step 3
5. for step 2 
    a. the output data is processed and using the data is created as JSON with keys.
    b. the processed JSON data is the use to generate only the patch Names list for both the types
6. using the patch list generate the info for each inside a single file to process the pkg info's
    "cat /tmp/temp-patchlist.txt | grep -Ev "^$" | xargs zypper patch-info > /tmp/temp-patchlistinfo.txt"
7. The file from set 6 is used as below
    a. the output data is processed and using python the data is crawled to build as a JSON file from txt.
    b. the same JSON is again processed with proper structuring with object and keys
8. Now from step 5 the data is again processed with python using the package name and both sev and category is identified
9. all saved vars - pkg, sev, cat, current version, new version, arch are getting saved into a csv file.
10. From step 7 the data is converted into a JSON key based array.
11. data is passed to the API calls



| Automation   | SLES 15.4   | SLES 15.5   | OpenSUSE 15   | SLES 12.5  |
|:---:|:---:|:---:|:---:|:---:|
| RMT   | Y  | Y  |   |   |
| Patch Scan   | Y  |   | Y  |   |
| Patch Deploy  | Y  |   |   |   |
