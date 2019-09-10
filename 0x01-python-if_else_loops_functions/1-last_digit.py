#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
l = string_number[-1:]
if int(l) > 5:
    print("Last digit of {} is {} and is greather than 5".format(number, l))
elif int(l) == 0:
    print("Last digit of {} is {} and is 0".format(number, l))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, l))
