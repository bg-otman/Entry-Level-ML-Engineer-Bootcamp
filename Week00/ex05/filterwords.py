import sys
import string

def is_valid_args(args):
    if len(args) != 2 or (args[0].isdigit() or not args[1].isdigit()):
        sys.exit("ERROR")

is_valid_args(sys.argv[1:])

final_list = []

def remove_punct(str):
    for i in range(len(str)):
        if str[i] in string.punctuation:
            return str[:i]
    else:
        return str

def add_to_list(S, N):
    if len(S) > N:
        final_list.append(S)

def filter_words(S, N):
    sep_list = S.split(" ")
    for i in range(len(sep_list)):
        sep_list[i] = remove_punct(sep_list[i])
        add_to_list(sep_list[i], N)
    else:
        return final_list

print(filter_words(sys.argv[1], int(sys.argv[2])))