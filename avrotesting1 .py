import os
import json

# Directory containing JSON files
json_dir = "/home/bipinpreetsingh/dsl-schema-main/schemas/"

# Process JSON files one by one
for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        json_path = os.path.join(json_dir, filename)

        with open(json_path, "r") as json_file:
            data = json.load(json_file)

            # Serialize the names and types of fields
            field_info = {}
            for key, value in data.items():
                field_type = type(value).__name__
                field_info[key] = field_type

            # Output the serialized field information
            print(f"File: {filename}")
            for field_name, field_type in field_info.items():
                print(f"Field Name: {field_name}, Type: {field_type}")
print("Serialization completed.")
