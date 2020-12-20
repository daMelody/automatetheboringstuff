import sys


def collatz(number):
    #* note to self: % is the modulus sign...
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = (3 * number) + 1
        print(number)
        return number


try:
    user_input = int(input("Enter number: "))
    while user_input != 1:
        user_input = collatz(user_input)
except ValueError:
    print("User must enter an integer value")
