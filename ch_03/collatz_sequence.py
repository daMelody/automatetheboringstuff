def collatz(number):
    if number // 2 == 0:
        number = number / 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number


user_input = int(input("Enter number: "))

while user_input != 1:
    user_input = collatz(user_input)
