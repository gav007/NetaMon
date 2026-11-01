import time

def complete(choice):

    if choice == 1:
        tool = "OS MODULE"
        filename = "local_network_os.json"

    elif choice == 2:
        tool = "SUBPROCESS"
        filename = "local_network_subprocess.json"

    elif choice == 3:
        tool = "PEXPECT"
        filename = "local_network_pexpect.json"

    else:
        return

    print("\n    [ NETAMON ] Processing", end="", flush=True)

    for i in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)

    print("""

    ============================================
                 N E T A M O N
    ============================================

             [✓] OPERATION COMPLETE

    --------------------------------------------
    """)

    print("    [+] Tool:    ", tool)
    print("    [+] Status:   SUCCESS")
    print("    [+] File:    ", filename)

    print("""
    --------------------------------------------

       Your network data has been saved!

       Location: ./data/

    ============================================

          >>> MISSION ACCOMPLISHED <<<

    """)
