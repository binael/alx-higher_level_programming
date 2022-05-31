#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

if (number < 0):
    last = -1 * ((number * -1) % 10)
else:
    last = number % 10

print(f"Last digit of {number:d} is {last:d}", end=" ")

if (last == 0):
    print("and is 0")
elif (last > 5):
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
