import json

def create_os_text_doc():

    with open("data/local_network.json", "r") as f:

        data = json.load(f)

    with open("data/network_report.txt", "w") as f:

        f.write("NETAMON NETWORK REPORT\n")
        f.write("======================\n")

        # get hostname

        hostname = data.get("hostname")

        if hostname:

            f.write("[+] Hostname: " + hostname + "\n")

        else:

            f.write("[-] Hostname not found!\n")


        for interface in data["interfaces"]:

            f.write("[*] Checking interfaces!\n")

            # get interface

            interface_name = interface.get("ifname")

            if interface_name:

                f.write("[+] Interface: " + interface_name + "\n")

            else:

                f.write("[-] interface name missing!\n")


            # get address

            address = interface.get("address")

            if address:

                f.write("[+] MAC: " + address + "\n")

            else:

                f.write("[-] MAC missing!\n")


            # get MTU

            mtu = interface.get("mtu")

            if mtu:

                f.write("[+] MTU: " + str(mtu) + "\n")

            else:

                f.write("[-] MTU missing!\n")


            # get MTU

            operation_state = interface.get("operstate")

            if operation_state and operation_state == "UP":

                f.write("[+] Operation State: " + operation_state + "\n")

            else:

                f.write("[-] " + operation_state + "\n")


create_os_text_doc()
