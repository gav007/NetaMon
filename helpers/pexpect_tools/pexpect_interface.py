import re
import pexpect
import json

def run_pexpect_interface():

    get_links = pexpect.run("ip -color=never link show")
    links_decoded = get_links.decode()
    #print(links_decoded)

    get_route = pexpect.run("ip -json route show")
    route_decoded = get_route.decode()
    #print(route_decoded)

    get_host = pexpect.run("hostname")
    host_decoded = get_host.decode().strip()
    #print(host_decoded)

    ### PATTERNS ###
    host_name = (r"\d+:\s(\w+):")
    mtu_name = (r"mtu\s(\d+)")
    MAC_name = (r"/\w+\s+([a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2}:[a-f0-9]{2})")
    flag_name = (r"<([\w,]+)>")
    opState_name = (r"state\s(\w+)")

    ipv4 = (r"inet\s([\d.]+)")
    ipv6 = (r"inet6\s([a-fA-F0-9:]+)")

    ### END ###
 
    interfaces = {}

    interfaces["hostname"] = host_decoded
    interfaces["interface"]=[]

    ### COMPILE PATTERNS ##

    ## HOSTNAME LINK RETURNS LIST##
    find_host = re.compile(host_name)
    str_host = re.findall(find_host, links_decoded) ## how many interfaces
    #print(str_host)
    ## FIN HOSTNAME LINK ##

    ## MTU LINK RETURNS LIST##
    find_mtu = re.compile(mtu_name)
    int_mtu = re.findall(find_mtu, links_decoded)
    #print(int_mtu)
    ## FIN MTU LINK ##

    ## MAC LINK RETURNS LIST##
    find_MAC = re.compile(MAC_name)
    str_MAC = re.findall(find_MAC, links_decoded)
    #print(str_MAC)
    ## FIN MAC LINK ##

    ## FLAG LINK RETURNS LIST##
    find_flag = re.compile(flag_name)
    str_flag = re.findall(find_flag, links_decoded)
    flag_dict = {}
    flag_dict["flags"]=[]
    for i in str_flag:
        new_flag = i.split(",")
        flag_dict["flags"].append(new_flag)
    #print(json.dumps(flag_dict, indent=4))
    #print(str_flag)
    ## FIN FLAG LINK ##

    ## STATE LINK RETURNS LIST##
    find_state = re.compile(opState_name)
    str_state = re.findall(find_state, links_decoded)
    #print(str_state)
    ## FIN STATE LINK ##


    ### END ###


    for interface in range(len(str_host)):
        #print(interface)
        interface_data_filter = {}
 
        interface_data_filter["name"]=str_host[interface]
        interface_data_filter["mtu"]=int(int_mtu[interface])
        interface_data_filter["mac"]=str_MAC[interface]
        interface_data_filter["flags"]=flag_dict["flags"][interface] # from above
        interface_data_filter["state"]=str_state[interface]

        name = str_host[interface]
        one_address = pexpect.run("ip -color=never address show " + name).decode()

        interface_data_filter["ipv4"] = re.findall(ipv4, one_address)
        interface_data_filter["ipv6"] = re.findall(ipv6, one_address)
        



        interfaces["interface"].append(interface_data_filter)

    #print(json.dumps(interfaces,indent=4))
    return interfaces

#run_pexpect_interface()
