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
    operator = tokens[0]
    num1 = int(tokens[1])
    num2 = int(tokens[2])
    if operator == "q":
        break
    elif operator == "+":
        print(add(num1, num2))
    elif operator == "-":
        print(subtract(num1, num2))
