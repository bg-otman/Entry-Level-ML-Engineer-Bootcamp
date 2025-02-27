from time import sleep, perf_counter
from math import ceil

start = perf_counter()

def calculate_eta(progress, elapsed, remaining_prog):
    return (elapsed / progress) * remaining_prog

def bar_progress(progress_percent):
    bar_length = 35
    num_equals = round(ceil((progress_percent / 100) * bar_length))
    bar = "" * bar_length
    for i in range(bar_length):
        if i < num_equals - 1:
            bar += '='
        else:
            bar += ' '
    else:
        return bar.replace(" ", ">", 1)

def ft_progress(listy):
    progress = 1
    prog_len = len(listy)
    for item in listy:
        elapsed = perf_counter() - start
        eta = calculate_eta(progress, elapsed, prog_len - progress)
        progress_percent = round(ceil((progress / prog_len) * 100))
        print(f"ETA: {eta:.2f}s [{progress_percent:d}%][\033[32m{bar_progress(progress_percent)}\033[0m] {progress}/{prog_len} | elapsed time {elapsed:.2f}s", end='\r')
        progress += 1
        yield item

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
