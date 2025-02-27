kata = (19, 42, 21)

def print_tuple_content(tuple):
    print(f"The {len(tuple)} numbers are: ", end="")
    for i in range(len(tuple) - 1):
        print(tuple[i], end=", ")
    else:
        print(tuple[i + 1], end="\n")

print_tuple_content(kata)