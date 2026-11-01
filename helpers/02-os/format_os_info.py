import json
import os

def format_os_info(interfaces, addresses, routes):
    my_data = {
           "hostname": "",
           "interfaces": [],
           "addresses": [],
           "routes": []
           }

    host = os.popen("hostname").read().strip()

    my_data["hostname"] = host

    for interface in interfaces:
        my_data["interfaces"].append(interface)

    for route in routes:
        my_data["routes"].append(route)

    for address in addresses:
        my_data["addresses"].append(address)

    # add ip address to interfaces
    for interface in my_data["interfaces"]:
        for address in my_data["addresses"]:
            if interface["ifname"] == address["ifname"]:
                interface["addr_info"] = address["addr_info"]

    # remove address from data
    my_data.pop("addresses")

    return my_data
