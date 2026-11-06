# TESTING NOT USED

from sub_interface import run_sub_interface
from sub_file_out import sub_file_out
import json

def main():

    results = run_sub_interface()

    sub_file_out(results)

if __name__ == "__main__":
    main()
