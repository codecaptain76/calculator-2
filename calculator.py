"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while True:
    input = raw_input("> ")
    tokens = input.split(" ")
    num_operands = len(tokens)-1
    operator = tokens[0]
    
    for n in range(num_operands):
        if "." in tokens[n+1]:
            num1 = float(tokens[n+1]) # need to figure out how to increment variable names
        else:
            num1 = int(tokens[n+1])     # same as above

    # if "." in tokens[-1]:
    #     num2 = float(tokens[-1])
    # else:
    #     num2 = int(tokens[-1])
    
    if operator == "q":
        break
    elif operator == "+":
        print add(num1, num2)
    elif operator == "-":
        print subtract(num1, num2)
    elif operator == "*":
        print multiply(num1, num2)
    elif operator == "/":
        print divide(num1, num2)
    elif operator == "square":
        print square(num1)
    elif operator == "cube":
        print cube(num1)
    elif operator == "power":
        print power(num1, num2)
    elif operator == "mod":
        print mod(num1, num2)
    else:
        print "I don't understand"


