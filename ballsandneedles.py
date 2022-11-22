# Author: Ben Lilley

from sys import stdin
from collections import defaultdict

table_2d = defaultdict(lambda: set())
table_3d = defaultdict(lambda: set())
for line in stdin:
    break

# For every edge, add it to the 3d or 2d graph. Make sure it is not
# a self edge before entering it into the graph table.
for line in stdin:
    a,b,c,d,e,f = map(int,line.split(" "))
    if (a,b,c) != (d,e,f):
        table_3d[(a,b,c)].add((d,e,f))
        table_3d[(d,e,f)].add((a,b,c))
    else:
        if (a,b,c) not in table_3d:
            table_3d[(d,e,f)] = set()
    if (a,b) != (d,e):
        table_2d[(a,b)].add((d,e))
        table_2d[(d,e)].add((a,b))
    else:
        if (a,b) not in table_2d:
            table_2d[(a,b)] = set()

table_2d = dict(table_2d)
table_3d = dict(table_3d)

# A simple DFS algorithm to check if there is a cycle. Iterative solution due to
# python recursive limitations. Visits all child nodes using DFS, if it ever occurs a
# node already visited (and was not the last node we came from), it returns true. Otherwise false
def dfs_cycle(graph, node, visited):
    stack = [(node,None)]
    visited[node] = True
    while stack:
        val = stack.pop(~0)
        for child in graph[val[0]]:
            if not visited[child]:
                visited[child] = True
                stack.append((child,val[0]))
            elif val[1] != child:
                return True
    return False

# Check if the given graph has any cycles using the dfs_cycle algorithm
def check(graph):
    visited = {}
    for key in graph:
        visited[key] = False
    for item in graph:
        if not visited[item]:
            if dfs_cycle(graph, item, visited):
                return True
    return False
# Run our code to determine the appropriate outputs
print("True closed chains" if check(table_3d) else "No true closed chains")
print("Floor closed chains" if check(table_2d) else "No floor closed chains")
