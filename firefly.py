#Author: Ben Lilley

from sys import stdin
from collections import Counter

# Grabbing the height of the cave
for line in stdin:
    _,h = map(int, line.split(" "))
    break

# Turn the stdin to a list of integers
lines = list(map(int, stdin))

# min_obstacles and levels_min_appears represent our two variables we are printing,
# the minimum number of obstacles we can hit and on how many floors this can be achieved
min_obstacles = 10000000000
levels_min_appears = 0

# neg_accum keeps track of our accumulation for the stalagmites on the ground, since
# all stalagmites with a larger int representation are counted when going through a levels
# The initial neg_accum is the amount of these stalagmites (len(lines) // 2). accum
# works conversly for the stalagmites on the top of the cave.
neg_accum = len(lines) // 2
accum = 0

# Our "up" stalagmites (top of cave) and the stalagmites "down" (bottom of cave) counted
up = Counter(lines[0::2])
down = Counter(lines[1::2])

# Loop through the heights possible
for i in range(0,h):
    # Our new up value is the running sum of accum plus our current value, our
    # new down value is our negative accumulation
    nu = accum + up[h-i]
    nd = neg_accum

    # Our hit value is the amount of hits (nu, nd) combined
    val = nd + nu
    # Set our min_obstacles and levels_min_appears appropriately (minimum logic)
    if val < min_obstacles:
        min_obstacles = val
        levels_min_appears = 1
    elif val == min_obstacles:
        levels_min_appears += 1
    # Set the next accum and neg_accum
    accum = nu
    neg_accum -= down[i+1]
print(min_obstacles,levels_min_appears)
