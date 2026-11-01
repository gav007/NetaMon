from format_os_info import format_os_info
from os_address_run import run_os_address
from os_link_run import run_os_link
from os_route_run import run_os_route
from os_file_out import os_file_out
import json

def main():

    route = run_os_route()
    address = run_os_address()
    interface = run_os_link()

    big_data = format_os_info(interface, address, route)
    #print(json.dumps(big_data,indent=4))
    os_file_out(big_data)

if __name__ == "__main__":
    main()
