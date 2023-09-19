import os
import json

# Specify the directory path where your JSON files are located
directory_path = '/home/bipinpreetsingh/Pythontasks/dsl-schema-main/schemas/'

# List all files in the directory
all_files = os.listdir(directory_path)

# Filter JSON files
json_files = [file for file in all_files if file.endswith('.json')]
# Process each JSON file one by one
for json_file in json_files:
    file_path = os.path.join(directory_path, json_file)
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        try:
            json_data = json.load(file)
            # Now you can work with the JSON data in the 'json_data' variable
            print(f"Processing {json_file}:")
            print(json_data)
        except json.JSONDecodeError as e:
            print(f"Error reading {json_file}: {e}")