def display():

    print(r"""
    _   _      _        __  __
   | \ | | ___| |_ __ _|  \/  | ___  _ __
   |  \| |/ _ \ __/ _` | |\/| |/ _ \| '_ \
   | |\  |  __/ || (_| | |  | | (_) | | | |
   |_| \_|\___|\__\__,_|_|  |_|\___/|_| |_|

    N E T W O R K   M O N I T O R
    =========================================
        SYSTEM RECONNAISSANCE CONSOLE
    =========================================


                   [ LOCAL HOST ]
                         |
                  +------+------+
                  |             |
             [ NETWORK ]    [ SYSTEM ]
                  |             |
             [ INTERFACES ] [ ROUTES ]
                  |             |
                  +------+------+
                         |
                    [ NETAMON ]
                         |
                    [ JSON DATA ]


    +---------------------------------------+
    |          SELECT YOUR TOOL             |
    +---------------------------------------+
    |                                       |
    |   [1]  OS MODULE                      |
    |   [2]  SUBPROCESS                     |
    |   [3]  PEXPECT                        |
    |                                       |
    |   [0]  EXIT SYSTEM                    |
    |                                       |
    +---------------------------------------+

    >>> AWAITING USER COMMAND <<<
    """)

    valid_choices = [0, 1, 2, 3]
    number = 1
    
    while number == 1:

        try:
            choice = int(input("    NetaMon@UbuntuGav:~$ "))

            if choice in valid_choices:
                
                number = 0

            else:
                
                print("Please select 0, 1, 2 or 3")

        except ValueError:
            print("Please enter a valid number")
            
    return choice
