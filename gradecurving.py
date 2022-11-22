# Author: Ben Lilley

from sys import stdin
from math import ceil

# Given recursive function
# lim f(x) = 100
def f(x):
    return 10 * (x ** (0.5))

for line in stdin:
    # Grab our initial value, and the low and high of our range
    x,y_l,y_h = map(int, line.split(" "))
    # The minimum iterations it takes to get in our range and the max it takes
    # to stay in it
    min_k, max_k = -1, 0
    times = 0
    while True:
        if times != 0:
            x = f(x)
        # If we are between our range
        if y_l <= ceil(x) and ceil(x) <= y_h:
            # If this is the first time we entered the range, change min_k
            if min_k == -1:
                min_k = times
                # If our upper bound is 100, we will never escape, thus giving us "min_k inf"
                if y_h == 100:
                    print(min_k, "inf")
                    break
            # Set max_k to current iteration
            max_k = times
        # If we are past our range
        elif ceil(x) > y_h:
            # If we never went through it, it is impossible since the function is
            # always increasing. If we did go through it, we can safely print out
            # our two notable values
            if min_k == -1:
                print("impossible")
            else:
                print(min_k, max_k)
            break
        times += 1
