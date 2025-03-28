import json
import os

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_all_json_files(file_path):
    jlist = []
    for file in os.listdir(file_path):
        full_file_path = "%s/%s" % (file_path, file)
        data = read_json(full_file_path)
        jlist.append(data)
    
    return jlist

def write_pickle(file_path, data):
    json_object = json.dumps(data)
    with open("golden_output.pickle", mode = "w") as outfile:
        outfile.write(json_object)

def load_pickle(file_path):
    with open(file_path, 'r') as file:
        pickle = json.load(file)
    print(pickle)
    # f = open(file_path)
    # data = json.load(f)

    # for i in data:
    #     print(i)

    # f.close