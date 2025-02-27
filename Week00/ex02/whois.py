import sys

args = sys.argv[1:]
def arg_nums(args_len):
    if (args_len == 0):
        sys.exit()
    assert args_len == 1, "AssertionError : more than one argument is provided"

def is_digit(arg):
    assert arg.isdigit(), "AssertionError : argument is not an integer"

def is_odd(num):
    return (num % 2 != 0)

try:
    arg_nums(len(args))
except AssertionError as msg:
    print(msg)
    sys.exit()

try:
    is_digit(args[0])
except AssertionError as msg:
    print(msg)
    sys.exit()

num = int(args[0])
if (num == 0):
    print("I'm Zero.")
elif (is_odd(num)):
    print("I'm Odd.")
else:
    print("I'm Even.")
