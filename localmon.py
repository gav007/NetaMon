# Modules
import sys
import time
import subprocess

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

# Summary
from summary import summary_sub

# Clear
from helpers.clear import clear_screen

def main():

    # if users_selection == 1:
        
    #     try:
    #         # Get Route Info
    #         route = run_os_route()
            
    #         # Get Address Info
    #         address = run_os_address()
            
    #         # Get Interface Info
    #         interface = run_os_link()

    #         # Format the data
    #         big_data = format_os_info(interface, address, route)

    #         # Data out ==> File
    #         os_file_out(big_data)

    #     except:
    #         print("Banjaxed somewhere, call the admin..")

    # elif users_selection == 2:
        
    #     try:
    #         # All command here, not modular yet
    #         subprocess_data = run_sub_interface()
        
    #         # Data Out ==> File
    #         sub_file_out(subprocess_data)

            

    #     except:
    #         print("Banjaxed somewhere, call the admin..")

    # elif users_selection == 3:
    
    #     try:
    #         # All command here, not modular yet
    #         pexpect_data = run_pexpect_interface()
            
    #         # Data Out ==> File
    #         pexpect_file_out(pexpect_data)

    #     except:
    #         print("Banjaxed somewhere, call the admin..")

    # elif users_selection == 0:
    #     print("Shutting down NetaMon...")
    #     sys.exit(0)

    # Run SUBPROCESS
    users_selection = display()
    time.sleep(5)

    clear_screen()
    try:
        # All command here, not modular yet
        subprocess_data = run_sub_interface()
            
        # Data Out ==> File
        sub_file_out(subprocess_data)

        complete(users_selection)
        time.sleep(5)
        clear_screen()
        summary_sub()
                
    
    except subprocess.CalledProcessError as error:
        print("Banjaxed somewhere, call the admin..", error)


    # # clear    
    # clear_screen() 
        
       
    # if users_selection in [1, 2, 3]:
        
    #     complete(users_selection)
    #     time.sleep(5)
    #     clear_screen()
    #     if users_selection == 2:
    #         summary_sub()
        

if __name__ == "__main__":
    main()
