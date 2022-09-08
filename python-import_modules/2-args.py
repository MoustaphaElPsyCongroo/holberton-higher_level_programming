#!/usr/bin/python3
import sys
argv = sys.argv
argv_len = len(argv) - 1

if __name__ == "__main__":
    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print(f"1 argument:\n1: {argv[1]}")
    else:
        print(f"{argv_len} arguments:")

        for i, arg in enumerate(argv):
            if i == 0:
                continue
            print(f"{i}: {arg}")
