#!/usr/bin/python3
import random
numb0er = random.randint(-10000, 10000)
last_number = abs(number) % 10
if last_number < 0:
    last_number = -last_number
    print(f"Last digit of {number} is {last_number} and is ", end = "")
if last_number > 5:
    print("greater than 5")
elif last_number == 0:
    print("0")
else:
    print("less than 6 and not 0")
