import os
import json


def run_os_address():
    
    interfaces = []

    command = os.popen("ip -json address show")
    output = command.read()

    data = json.loads(output)

    #print(json.dumps(data, indent=2))

    for line in data:
        interface = {}
        for key, value in line.items():
            if key == "ifname":
                interface[key]=value
            if key == "addr_info":
                interface[key]=value
        interfaces.append(interface)

    unwanted = [ "scope", "dynamic", "noprefixroute", "label", "valid_life_time", "preferred_life_time"]
    
    # remove the crap from the addr_info
    for line in interfaces:
        for address in line["addr_info"]:
            for key in unwanted:
                address.pop(key, None)

    #print(json.dumps(interfaces,indent=2))
    return interfaces
#run_os_address()
