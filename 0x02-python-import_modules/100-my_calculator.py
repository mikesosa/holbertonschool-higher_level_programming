#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    args = argv[1:]
    result = 0
    length = len(argv)

    if(length != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[0])
    operator = args[1]
    b = int(args[2])
    if(operator == "+"):
        result = a + b
    elif(operator == "-"):
        result = a - b
    elif(operator == "*"):
        result = a * b
    elif(operator == "/"):
        result = a / b
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
    exit(0)
