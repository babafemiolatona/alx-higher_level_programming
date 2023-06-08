#!/usr/bin/python3
import sys

sum = 0

if __name__ == "__main__":
    for i in sys.argv[1:]:
        sum += int(i)
    print(sum)
