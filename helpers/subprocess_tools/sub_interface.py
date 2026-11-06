import json
import subprocess

def run_sub_interface():

    # get link info
    link_command = subprocess.run(["ip", "-json", "link", "show"], capture_output=True, text=True, check=True)
    link_result = json.loads(link_command.stdout)       # print(json.dumps(link_result,indent=4))
    

    # get address info
    
    address_command = subprocess.run(["ip", "-json", "address", "show"], capture_output=True, text=True, check=True)
    address_result = json.loads(address_command.stdout)
    # print(json.dumps(address_result,indent=4))

    

    # get route info
    
    route_command = subprocess.run(["ip", "-json", "route", "show"], capture_output=True, text=True, check=True)
    route_result = json.loads(route_command.stdout)
    # print(json.dumps(route_result,indent=4))

   
    # get hostname

    host_command = subprocess.run(["hostname"], capture_output=True, text=True, check=True)
    host = host_command.stdout.strip()
    #print(host)
    
    network_data = {
             "hostname": "",
              "interface": []
             }

    network_data["hostname"]=host
    

    for link in link_result:

        interface_info = {}
        
        # build the interface with the link_result data
        # .get() returns the value when given the key

        interface_info["name"]=link.get("ifname")
        interface_info["mtu"]=link.get("mtu")
        interface_info["mac"]=link.get("address")
        interface_info["flags"]=link.get("flags")
        interface_info["state"]=link.get("operstate")

        # build the interface with the address_result data
        interface_info["ip_addresses"]=[]

        for address in address_result:
            if address["ifname"] == interface_info["name"]:
                for ip in address["addr_info"]:
                    ips = {}
                    ips["family"]=ip["family"]
                    ips["local"]=ip["local"]
                    ips["prefixlen"]=ip["prefixlen"]
                    interface_info["ip_addresses"].append(ips)
        
        # get the route info data
        interface_info["routes"]=[]

        for route in route_result:
            if route["dev"] == interface_info["name"]:

                route_info = {}

                route_info["destination"]=route.get("dst")
                route_info["gateway"]=route.get("gateway")
                route_info["protocol"]=route.get("protocol")

                interface_info["routes"].append(route_info)

        network_data["interface"].append(interface_info)
    #print(json.dumps(network_data,indent=4))

    return network_data

#run_sub_interface()
