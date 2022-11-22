# Author: Ben Lilley

from sys import stdin

# Simple iterative binary search (recursive binary search is too slow). If the
# value is found, it will return true, else false.
def bin_search(arr, term):
    l,r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == term:
            return True
        elif term < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return False

for line in stdin:
    # Grab our sequence values
    n,m,a,c,x_0 = map(int, line.split(" "))
    last = x_0
    arr = []
    # Generate the recursive sequence to the nth term in our arr array
    for i in range(n):
        last = ((a * last + c) % m)
        arr.append(last)
    # For every value in the sequence, run binary search on it to determine
    # if it can be found. If it can, add one to our total.
    total = 0
    for term in arr:
        total += bin_search(arr, term)
    print(total)
