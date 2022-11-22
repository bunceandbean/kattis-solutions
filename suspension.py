# Author: Ben Lilley

from sys import stdin
import math

# Grab our d and s values
for line in stdin:
    d,s = map(int,line.split(" "))

# Set a reasonable bound for root searching. The slack length has to be positive (bottom = 0),
# and the max (top) was roughly determined by saying max(d) * max(s).
bottom = 0
top = 1000*1000

# Our function we are finding the roots of. The rearrangement of a + s = a * cosh(d/(2a)).
# We are looking for the variable a
def for_a(a):
    return a * math.cosh(d/(2 * a)) - a - s

# Bisection algorithm. Find the mid point, if the signs of f(mid) and f(top) are different, our
# root is from [mid, top]. Thus say bottom = mid and vice versa. If our mid value is within
# our error amount given, we consider it good enough to be our value of a.
while True:
    mid = (top + bottom) / 2
    if for_a(mid) * for_a(top) < 0:
        bottom = mid
    else:
        top = mid
    if abs(for_a(mid)) <= .00001:
        break
# Print l(a,d) now that we have an estimate of a
print(2 * mid * math.sinh(d/(2 * mid)))
