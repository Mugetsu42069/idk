import os

# Specify the directory path
directory_path = "/home/bipinpreetsingh/Pythontasks/dsl-schema-main/schemas/"
files = os.listdir(directory_path)
for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            print(file)
