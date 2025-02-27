import sys

args = sys.argv[1:]
if (len(args) == 0):
    sys.exit()
args = ' '.join(args).swapcase()[::-1]
print(args)