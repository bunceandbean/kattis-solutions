from sys import stdin

for line in stdin:
    amt = int(line)
    break

ignore = True
nums = -1
arr = []
for line in stdin[1:]:
    if ignore:
        out,nums = map(int, line.split(" "))
        arr = []
        ignore = not ignore
    else:
        if len(arr) != nums:
            arr += list(map(int,line.split(" ")))
        if len(arr) == nums:
            sorted_arr = sorted(arr)
            j = 0
            for i in range(len(arr)):
                if arr[i] == sorted_arr[j]:
                    j += 1
            print(out,len(arr)-j)
            ignore = not ignore
