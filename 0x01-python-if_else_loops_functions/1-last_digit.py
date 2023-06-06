#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last = abs(number) % 10

if int(number) < 0:
    last = -last

if last > 5:
    print(f"Last digit of {number_str} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number_str} is {last} and is 0")
elif (last < 6 and last != 0):
    print(f"Last digit of {number_str} is {last} and is less than 6 and not 0")
