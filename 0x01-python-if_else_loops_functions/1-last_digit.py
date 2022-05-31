#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
last = number % 10
str = f"Last digit of {number:d} is {last:d}"
if last > 5:
    print(f"{str} and is greater than 5")
elif last == 0:
    print(f"{str} and is 0")
elif last < 6 and last != 0:
    print(f"{str} and is less than 6 and not 0")
