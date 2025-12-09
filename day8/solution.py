from math import dist, prod
from collections import defaultdict

with open('input.txt') as f:
    lines = f.readlines()
    
# Part 1
"""
boxes = []
for i in lines:
    boxes.append([int(x) for x in i.strip().split(',')])
connected = []
distance = []
for i in range(len(boxes)):
    for j in range(i + 1,len(boxes)):
        if i != j:
            distance.append([dist(boxes[i], boxes[j]), {i, j}])

distance = sorted(distance)

for i in distance[:1000]:
    connected.append(i[1])

# print(connected)
def merge_shared(tuples_list):
    adj = defaultdict(set)

    # build graph
    for t in tuples_list:
        for x in t:
            adj[x].update(t)

    visited = set()
    groups = []

    def dfs(node, group):
        visited.add(node)
        group.add(node)
        for nxt in adj[node]:
            if nxt not in visited:
                dfs(nxt, group)

    for t in tuples_list:
        for x in t:
            if x not in visited:
                group = set()
                dfs(x, group)
                groups.append(tuple(sorted(group)))

    return groups
connected = merge_shared(connected)
ans = [len(x) for x in connected]
ans = sorted(ans)
# print(ans, connected)
print(prod(ans[-3:]))
"""

# Part 2

boxes = []
for i in lines:
    boxes.append([int(x) for x in i.strip().split(',')])
connected = []
distance = []
for i in range(len(boxes)):
    for j in range(i + 1,len(boxes)):
        if i != j:
            distance.append([dist(boxes[i], boxes[j]), [i,j]])

distance = sorted(distance)
seen = set()
ans = 0
for i in distance:
    if i[1][0] not in seen or i[1][1] not in seen:
        seen.add(i[1][0])
        seen.add(i[1][1])
        ans = boxes[i[1][0]][0] * boxes[i[1][1]][0]

print(ans)