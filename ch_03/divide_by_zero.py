def safe_spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid Argument')


safe_spam.__doc__ = "A function that safely attempts to divide 42 by an input. Will print an error message if the input is 0"


def unsafe_spam(divide_by):
    return 42 / divide_by


unsafe_spam.__doc__ = "A function that attempts to divide 42 by an input. Will crash and burn if any errors occur."

print('Safe Spam')
print(safe_spam(2))
print(safe_spam(0))  #? why does it work?
print('')

print('Mildly Unsafe Spam')
try:
    print(unsafe_spam(2))
    print(unsafe_spam(0))  #? what is happening here?
    print(unsafe_spam(1))  #? why doesn't this run?
except ZeroDivisionError:
    print('Error: Invalid Argument')
print('')

print('Unsafe Spam')
print(unsafe_spam(2))
print(unsafe_spam(0))  #? why doesn't it work?
