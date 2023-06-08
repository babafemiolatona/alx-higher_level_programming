#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    elif len(sys.argv) > 2:
        print(f"{len(sys.argv) - 1} arguments:")
        for i in sys.argv[1:]:
            print(f"{sys.argv.index(i)} : {i}")
