import string
import sys

class text:
    def __init__(self):
        self.printables = 0
        self.upper = 0
        self.lower = 0
        self.punct = 0
        self.spaces = 0

str_info = text()

def print_text_data():
    print(f"The text contains {str_info.printables} printable character(s):")
    print(f"- {str_info.upper} upper letter(s)")
    print(f"- {str_info.lower} lower letter(s)")
    print(f"- {str_info.punct} punctuation mark(s)")
    print(f"- {str_info.spaces} space(s)")

def is_not_string(arg):
    try:
        assert isinstance(arg, str), "AssertionError: argument is not a string"
    except AssertionError as msg:
        print(msg)
        return True

def text_analyzer(str = None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if (not str):
        print("What is the text to analyze ?")
        str = input(">> ")
    if is_not_string(str):
        return
    for char in str:
        if char.isprintable():
            str_info.printables += 1
        if char.isupper():
            str_info.upper += 1
        if char.islower():
            str_info.lower += 1
        if char.isspace():
            str_info.spaces += 1
        if char in string.punctuation:
            str_info.punct += 1
    else:
        print_text_data()
        str_info.__init__()

args = sys.argv[1:]
if len(args) > 1:
    print("Only one argument Allowed")
elif len(args) == 1:
    text_analyzer(args[0])
