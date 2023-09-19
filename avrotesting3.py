import os
import json
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

# Directory containing JSON files
json_dir = "/home/bipinpreetsingh/dsl-schema-main/schemas/"

# Output Avro directory
avro_dir = "/home/bipinpreetsingh/dsl-schema-main/avro_schemas/"

# Helper function to determine Avro type from Python type
def determine_avro_type(value):
    if isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "double"
    elif isinstance(value, bool):
        return "boolean"
    else:
        return "string"

# Process JSON files one by one
for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        json_path = os.path.join(json_dir, filename)

        with open(json_path, "r") as json_file:
            data = json.load(json_file)

            # Serialize the JSON data
            serialized_data = json.dumps(data)

            # Create Avro schema dynamically based on JSON data
            avro_fields = []
            for key, value in data.items():
                avro_type = determine_avro_type(value)
                avro_field = {
                    "name": key,
                    "type": avro_type
                }
                avro_fields.append(avro_field)

            avro_schema_dict = {
                "type": "record",
                "name": ""
            }
