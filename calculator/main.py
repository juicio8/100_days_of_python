from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {'+': add, '-': subtract, '/': divide, '*': multiply}


def calculator():
    print(logo)
    loop = True
    num1 = float(input("What's the first number? "))
    while loop:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number? "))

        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        should_loop = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start afresh or type 'o' to switch off.: ")
        if (should_loop == "y"):
            num1 = answer
        elif should_loop == "o":
            print("shutting down...")
            quit()
        else:
            loop = False
            calculator()


calculator()
