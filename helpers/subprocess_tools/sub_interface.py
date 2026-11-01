import json
import subprocess

def run_sub_interface():
    
    # get interface links
    link_command = subprocess.run(["ip", "-json", "link", "show"], capture_output=True, text=True)
    link_result = json.loads(link_command.stdout)
    # print(json.dumps(link_result,indent=4))

    # get address info

    address_command = subprocess.run(["ip", "-json", "address", "show"], capture_output=True, text=True)
    address_result = json.loads(address_command.stdout)
    # print(json.dumps(address_result,indent=4))

    # get route info
    route_command = subprocess.run(["ip", "-json", "route", "show"], capture_output=True, text=True)
    route_result = json.loads(route_command.stdout)
    # print(json.dumps(route_result,indent=4))

    # get hostname
    host_command = subprocess.run(["hostname"], capture_output=True, text=True)
    host = host_command.stdout.strip()
    #print(host)

    interfaces = {
             "hostname": "",
              "interface": []
             }

    interfaces["hostname"]=host
    

    for link in link_result:

        interface = {}
        
        # build the interface with the link_result data
        # .get() returns the value when given the key
        interface["name"]=link.get("ifname")
        interface["mtu"]=link.get("mtu")
        interface["mac"]=link.get("address")
        interface["flags"]=link.get("flags")
        interface["state"]=link.get("operstate")

        # build the interface with the address_result data
        interface["ip_addresses"]=[]
        for address in address_result:
            if address["ifname"] == interface["name"]:
                for ip in address["addr_info"]:
                    ips = {}
                    ips["family"]=ip["family"]
                    ips["local"]=ip["local"]
                    ips["prefixlen"]=ip["prefixlen"]
                    interface["ip_addresses"].append(ips)
        
        # get the route info data
        interface["routes"]=[]
        for route in route_result:
            if route["dev"] == interface["name"]:

                route_info = {}

                route_info["destination"]=route.get("dst")
                route_info["gateway"]=route.get("gateway")
                route_info["protocol"]=route.get("protocol")

                interface["routes"].append(route_info)

        interfaces["interface"].append(interface)
    #print(json.dumps(interfaces,indent=4))
    return interfaces
#run_sub_interface()
