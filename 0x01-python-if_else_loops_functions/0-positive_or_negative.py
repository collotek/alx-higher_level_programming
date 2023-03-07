#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for x in number:
    if x > 0:
        print(x 'is positive')
    elif x == 0:
        print(x 'is zero')
    else:
        print(x 'is negative')
