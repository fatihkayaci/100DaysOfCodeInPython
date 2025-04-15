import os
import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
    }
continue_calculating = ''
result = 0
clear = lambda: os.system('cls')
while True:
    if continue_calculating.lower() == 'n' or not continue_calculating:
        clear()
        print(art.logo)
        first_number = float(input("What's the first number?: "))
    else:
        first_number = result
    for key in operations:
        print(key)
    pick_operation = input("Pick in operation: ")
    second_number = float(input("What's the next number?: "))
    result = operations[pick_operation](first_number, second_number)
    print(f"{first_number} {pick_operation} {second_number} = {result}")
    
    continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    