import os
import json
from io import StringIO

def run_os_link():

    interfaces = []

    command = os.popen("ip -json link show")
    output = command.read()

    stream = StringIO(output)
    data = json.load(stream)

    #print(json.dumps(data, indent=4))
    #print(type(data))

    for line in data:
        interface = {}
        for key, value in line.items():
            if key == "ifname":
                interface[key]=value
            if key == "mtu":
                interface[key]=value
            if key == "address":
                interface[key]=value
            if key == "flags":
                interface[key]=value
            if key == "operstate":
                interface[key]=value
        interfaces.append(interface)
    #print(json.dumps(interfaces,indent=4))
    return interfaces

#run_os_link()
