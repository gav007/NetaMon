def display():

    print(r"""
 /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$
| $$$ | $$| $$_____/|__  $$__//$$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$
| $$$$| $$| $$         | $$  | $$  \ $$| $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$ $$ $$| $$$$$      | $$  | $$$$$$$$| $$ $$/$$ $$| $$  | $$| $$ $$ $$
| $$  $$$$| $$__/      | $$  | $$__  $$| $$  $$$| $$| $$  | $$| $$  $$$$
| $$\  $$$| $$         | $$  | $$  | $$| $$\  $ | $$| $$  | $$| $$\  $$$
| $$ \  $$| $$$$$$$$   | $$  | $$  | $$| $$ \/  | $$|  $$$$$$/| $$ \  $$
|__/  \__/|________/   |__/  |__/  |__/|__/     |__/ \______/ |__/  \__/
    
    
    Enter your choice:

    0. Exit the program
    1. OS Result
    2. Subprocess Result
    3. Pexpect Result
    
    """)

    valid_choices = [0, 1, 2, 3]
    number = 1
    
    while number == 1:

        try:
            choice = int(input(">>> "))

            if choice in valid_choices:
                
                number = 0

            else:
                
                print("Please select 0, 1, 2 or 3")

        except ValueError:
            print("Please enter a valid number")
            
    return choice
