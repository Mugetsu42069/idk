import os
import json
from avro import schema, datafile, io

# Directory containing JSON files
json_directory = "/home/bipinpreetsingh/dsl-schema-main/schemas/"

# Output directory for Avro schemas
avro_schema_directory = "/home/bipinpreetsingh/dsl-schema-main/avro_schemas/"

# Ensure the Avro schema directory exists
os.makedirs(avro_schema_directory, exist_ok=True)

# Iterate over each JSON file in the directory
for json_filename in os.listdir(json_directory):
    if json_filename.endswith(".json"):
        json_filepath = os.path.join(json_directory, json_filename)
        
        # Load JSON data from the file
        with open(json_filepath, "r") as json_file:
            json_data = json.load(json_file)
        
        # Define the Avro schema file path
        avro_schema_filename = os.path.splitext(json_filename)[0] + ".avsc"
        avro_schema_filepath = os.path.join(avro_schema_directory, avro_schema_filename)
        
