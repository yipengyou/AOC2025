"""
with open('input.txt', 'r') as f:
    content = f.readlines()
"""
# Part 1
"""
tiles = [[int(j) for j in i.strip().split(',')] for i in content]
ans = 0
for i in range(len(tiles)):
    for j in range(len(tiles[i + 1:])):
        area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
        ans = max(ans, area)
print(ans)
"""

# Part 2
"""
tiles = [[int(j) for j in i.strip().split(',')] for i in content]
ans = 0
for i in range(len(tiles)):
    for j in range(len(tiles[i + 1:])):
        area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
        ans = max(ans, area)
print(ans)
"""
# Gave up, cheating using someones solution instead
from itertools import combinations

with open('input.txt','r') as fo:
    vertices = [tuple(map(int, line.split(','))) for line in fo]
    
part1 = max((abs(x0-x1)+1)*(abs(y0-y1)+1) for (x0, y0), (x1, y1) in combinations(vertices,2))

edges = list(zip(vertices, vertices[1:]+[vertices[0]]))
vertical_edges = [(x0, *sorted((y0,y1))) for (x0,y0), (x1,y1) in edges if x0==x1]
horizontal_edges = [(y0, *sorted((x0,x1))) for (x0,y0), (x1,y1) in edges if y0==y1]

part2 = 0
for (x0, y0), (x1, y1) in combinations(vertices, 2): 
    min_x, min_y, max_x, max_y = min(x0, x1)+0.5, min(y0, y1)+0.5, max(x0, x1)-0.5, max(y0, y1)-0.5
    if not any(
        (min_x<=v_x<=max_x and (min_v_y<=min_y<=max_v_y or min_v_y<=max_y<=max_v_y)) or 
        (min_y<=h_y<=max_y and (min_h_x<=min_x<=max_h_x or min_h_x<=max_x<=max_h_x))
        for (v_x, min_v_y, max_v_y), (h_y, min_h_x, max_h_x) 
        in zip(vertical_edges, horizontal_edges)
    ):
        part2 = max(part2, (abs(x0-x1)+1)*(abs(y0-y1)+1))

print(part1, part2)