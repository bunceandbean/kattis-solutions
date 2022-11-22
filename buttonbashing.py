# Author: Ben Lilley

from sys import stdin
for line in stdin:
    break

# nums variable indicates if we are reading a test case or reading a test case set up data
nums = False
goal = -1
for line in stdin:
    if not nums:
        _,goal = map(int, line.split(" "))
    else:
        # If our goal is zero, we can simply press nothing
        if goal == 0:
            print(0,0)
            nums = not nums
            continue
        arr = list(map(int,line.split(" ")))
        best_path = float('inf')
        presses = float('inf')
        # This algorithm is an altered BFS algorithm. Therefore, we use a queue
        # to keep track of where we are in the paths and whether we still need to
        # consider a path. Our queue starts at a button with a value (path total weight)
        # of zero with zero presses
        q = [(0,0)]
        # Keep note of past path sums (vals/weights), if we have seen a sum before
        # do not put it back in the queue
        past_sums = set([0])
        done = False
        # While we have values in our queue
        while len(q) > 0:
            val = q.pop(0)
            # For every option in our next options (any button we want)
            for item in arr:
                next = val[0] + item
                # If the next total weight of the path puts us negative, we have no
                # reason to consider it a possibility
                if next < 0:
                    continue
                # If we went over or equal to our max, just consider it to be the max so we can use the past_sums logic on all values above the max
                elif next >= 3600:
                    next = 3600
                # If we hit the goal, we have our winner (BFS finds shortest path first). Print the presses and distance from the real goal
                if next == goal:
                    print(val[1] + 1, 0)
                    done = True
                    break
                # Else if we overshot or goal but still did better than our known best_path, readjust the new best path
                elif next > goal and next < best_path:
                    best_path = next
                    presses = val[1] + 1
                # If we haven't been to this summation before, evaluate it eventually by putting it in the queue
                if next not in past_sums:
                    past_sums.add(next)
                    q.append((next, val[1] + 1))
            if done:
                break
        if not done:
            # best_path - goal is the distance of the best path from our actual goal
            print(presses, best_path-goal)
    nums = not nums
