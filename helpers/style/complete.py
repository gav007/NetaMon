import time

def complete(choice):

    count_down = 5
    print()
    print("Running the Process, Hang tight!!\n")
    
    while count_down != 0:


        print(".", end=" ", flush=True)

        time.sleep(1)

        count_down -= 1

    print()
    print()

    print(r"""
     /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$
    | $$__  $$ /$$__  $$| $$$ | $$| $$_____/
    | $$  \ $$| $$  \ $$| $$$$| $$| $$      
    | $$  | $$| $$  | $$| $$ $$ $$| $$$$$   
    | $$  | $$| $$  | $$| $$  $$$$| $$__/   
    | $$  | $$| $$  | $$| $$\  $$$| $$      
    | $$$$$$$/|  $$$$$$/| $$ \  $$| $$$$$$$$
    |_______/  \______/ |__/  \__/|________/

     

    """)

    print()
    
    print(">>> Your file can be located in the ./data folder")

    print()

    print(">>> [+] Below you will find a summary")

    print()
