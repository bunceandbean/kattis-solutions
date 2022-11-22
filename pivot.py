# Author: Ben Lilley

from sys import stdin

# Grab the given array from stdin
i = 0
arr = []
for line in stdin:
    if i == 0:
        i +=1
        continue
    arr = list(map(int,line.split(" ")))


# Loop through array values. Check if the value is equal to the value it should be (i.e, arr[0] = 1)
# if it does, then it needs to be an endpoint or be greater than everything below it (the maximum value below it, max_cur)
# to add one to the count. If our value is not equal to its supposed value, check if the value is greater than max_cur, if it is,
# set max cur to that (maximum value below us).
count = 0
max_cur = -1
for i in range(len(arr)):
    if i + 1 != arr[i]:
        if arr[i] > max_cur:
            max_cur = arr[i]
        continue
    if i == 0 or i == len(arr) - 1 or max_cur < arr[i]:
        count += 1
print(count)
