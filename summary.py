import json

def summary_sub():
    with open("data/local_network.json", "r") as f:
        data = json.load(f)
        #print(data)
        hostname = data.get("hostname")
        #print(hostname)
        interface_list = data.get("interface")
        
        print("***************************")
        print("Summary Print Out")
        print("***************************")
        print()

        count = 1
        for interface in interface_list:
            interface_name = interface.get("name")
            mtu_value = interface.get("mtu")
            mac_daddy = interface.get("mac")
            operational_state = interface.get("state")
            flag_list = interface.get("flags")
            ip_addr_list = interface.get("ip_addresses")
            route_list = interface.get("routes")

            print("Interface Number", count)
            print()
            print("Interface Name:", interface_name)
            print("MTU Value:", mtu_value)
            print("MAC Address:", mac_daddy)
            print("Operational State:", operational_state)
            
            print()
            
            print("FLAGS")
            for flag in flag_list:
                
                print("-", flag)

            print()

            print("IPv4 and IPv6 Addresses")
            for ip in ip_addr_list:
                ip_address = ip.get("local")
                
                print("-", ip_address)

            print()

            print("Default Gateway")
            for route in route_list:
                gateway = route.get("gateway")
                if gateway != None:
                    print("-", gateway)
                

            print() 

            print("***************************")
            print()
            count += 1