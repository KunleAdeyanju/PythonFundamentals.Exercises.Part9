import json
import os

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_all_json_files(file_path):
    jlist = []
    for file in os.lisdir(file_path):
        full_file_path = "%s/%s" % (file_path, file)
        with open(full_file_path, 'r') as file2
        data = json.load(file2)
        jlist.append(data)
    
    return jlist
