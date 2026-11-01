# Modules
import sys

# Sub interface Tools

from helpers.subprocess_tools.sub_interface import run_sub_interface
from helpers.subprocess_tools.sub_file_out import sub_file_out

# OS Tools

from helpers.os_tools.format_os_info import format_os_info
from helpers.os_tools.os_address_run import run_os_address
from helpers.os_tools.os_link_run import run_os_link
from helpers.os_tools.os_route_run import run_os_route
from helpers.os_tools.os_file_out import os_file_out

# Pexpect Tools

from helpers.pexpect_tools.pexpect_interface import run_pexpect_interface
from helpers.pexpect_tools.pexpect_file_out import pexpect_file_out

# Style

from helpers.style.display import display
from helpers.style.complete import complete

def main():

    # Display a display menu. AI designed the display.
    users_selection = display()

    if users_selection == 1:
        
        # Get Route Info
        route = run_os_route()
        
        # Get Address Info
        address = run_os_address()
        
        # Get Interface Info
        interface = run_os_link()

        # Format the data
        big_data = format_os_info(interface, address, route)

        # Data out ==> File
        os_file_out(big_data)

    elif users_selection == 2:
    
        # All command here, not modular yet
        subprocess_data = run_sub_interface()
    
        # Data Out ==> File
        sub_file_out(subprocess_data)
        
    elif users_selection == 3:
    
        # All command here, not modular yet
        pexpect_data = run_pexpect_interface()
        
        # Data Out ==> File
        pexpect_file_out(pexpect_data)
    
    elif users_selection == 0:
        print("Shutting down NetaMon...")
        sys.exit(0)
        
        
        
    # Confirmation display, AI designed display    
    if users_selection in [1, 2, 3]:
        complete(users_selection)
        

if __name__ == "__main__":
    main()
