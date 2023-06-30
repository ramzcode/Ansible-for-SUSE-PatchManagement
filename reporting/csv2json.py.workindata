import csv
import json

def csv_to_json(csv_file_path, json_file_path, key_column):
    data = {}
    
    # Read the CSV file
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        # Convert each row to a dictionary and add it to the data dictionary
        for row in reader:
            key = row[key_column]
            del row[key_column]  # Remove the key column from the row dictionary
            data[key] = row
    
    # Write the data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
csv_file_path = '/tmp/errata.csv'
json_file_path = '/tmp/errata.json'
key_column = 'Package'  # Specify the column name to be used as the key
csv_to_json(csv_file_path, json_file_path, key_column)

