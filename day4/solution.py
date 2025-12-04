with open('input.txt', 'r') as f:
    content = f.readlines()

paperRolls = []
for i in content:
    paperRolls.append([x for x in i.strip()])

DIRS = [
    (-1,  0),  # up
    ( 1,  0),  # down
    ( 0, -1),  # left
    ( 0,  1),  # right
    (-1, -1),  # up-left
    (-1,  1),  # up-right
    ( 1, -1),  # down-left
    ( 1,  1),  # down-right
]

def surround(row, col):
    if row >= 0 and row < len(paperRolls) and col >= 0 and col < len(paperRolls[0]):
        if paperRolls[row][col] == '@':
            return 1
    return 0

# Part 1
"""
ans = 0
for row in range(len(paperRolls)):
    for col in range(len(paperRolls[0])):
        cnt = 0
        if paperRolls[row][col] == '.':
            continue
        for dir in DIRS:
            cnt += (surround(row + dir[0], col + dir[1]))
        #print(cnt)
        if cnt < 4:
            ans += 1
print(ans)
"""

# Part 2
ans = 0
removed = True
while removed == True:
    removed = False
    for row in range(len(paperRolls)):
        for col in range(len(paperRolls[0])):
            cnt = 0
            if paperRolls[row][col] == '.':
                continue
            for dir in DIRS:
                cnt += (surround(row + dir[0], col + dir[1]))
            #print(cnt)
            if cnt < 4:
                paperRolls[row][col] = '.'
                removed = True
                ans += 1
print(ans)