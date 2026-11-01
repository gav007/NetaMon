import json

def os_file_out(data):
    with open("data/local_network.json", "w") as f:
        json.dump(data, f, indent=4)
