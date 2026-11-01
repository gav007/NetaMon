import json

def pexpect_file_out(data):

    with open("data/local_network_pexpect.json", "w") as f:
        json.dump(data, f, indent=4)
