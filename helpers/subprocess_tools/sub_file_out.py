import json

def sub_file_out(data):
    with open("data/local_network_sub.json", "w") as f:
        json.dump(data, f, indent=4)
