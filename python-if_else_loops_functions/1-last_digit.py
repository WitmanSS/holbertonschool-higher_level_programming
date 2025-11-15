#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    lastDig = number % 10
else:
    lastDig = -int(str(number)[-1])

if lastDig > 5:
    case = "and is greater than 5"
elif lastDig == 0:
    case = "and is 0"
else:
    case = "and is less than 6 and not 0"

print(f"Last digit of {number} is {lastDig} {case}")
