# Author: Ben Lilley

from sys import stdin

# This variable keeps track of our current person to parse their data
person = 1
likes_1 = set()
likes_2 = set()

# Grab each movie for each person (person 1 and person 2) and put them in their respective set.
# If they have no liked movies, leave the "likes" set as empty.
for line in stdin:
    if person == 1:
        if " " in line:
            likes_1 = set(map(int, line[line.index(" ") +1:].split(" ")))
    else:
        if " " in line:
            likes_2 = set(map(int, line[line.index(" ") +1:].split(" ")))
    person = -1

# Merge the sets of their movies into one. Sort it to go in order.
movies = list(likes_1 | likes_2)
movies.sort()


best = 0
# The "weight" signifies who liked the last movie. With 1 being person 1, -1 being person 2,
# and 0 being both
weight = 0
count = 0
# Traverse each movie
for movie in movies:
    # If they both like the movie, we can increase our count of movies and set the weight to zero
    if movie in likes_1 and movie in likes_2:
        weight = 0
        count += 1
    # If only one likes it, add count and set weight if the weight isnt already in their favor
    elif movie in likes_1:
        if weight == 1:
            continue
        else:
            weight = 1
            count += 1
    elif movie in likes_2:
        if weight == -1:
            continue
        else:
            weight = -1
            count += 1
print(count)
