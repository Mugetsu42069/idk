import os
import json
directory_path = '/home/bipinpreetsingh/Downloads/dsl-schema-main/schemas/'
file_list = os.listdir(directory_path)
json_files = [file for file in file_list if file.endswith('.json')]