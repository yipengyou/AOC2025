with open("input.txt", 'r') as f:
    content = f.readlines()

beams = []
for i in content:
    temp = i.strip()
    beams.append([j for j in temp])

ans = 0
start = beams[0].index('S')
print(start)
row = 1
# Part 1
"""
while row < len(beams):
    for i in range(len(beams[row])):
        if beams[row - 1][i] == 'S':
            if beams[row][i] == '^':
                beams[row][i - 1] = 'S'
                beams[row][i + 1] = 'S'
                ans += 1
            else:
                beams[row][i] = 'S'
    row += 1
print(ans)
"""

# Part 2
beams[0][start] = 1
for i in range(len(beams)):
    for j in range(len(beams[i])):
        if beams[i][j] == '.':
            beams[i][j] = 0
while row < len(beams):
    for i in range(len(beams[row])):
        if beams[row - 1][i] != '^' and beams[row - 1][i] != 0:
            if beams[row][i] == '^':
                beams[row][i - 1] += beams[row - 1][i]
                beams[row][i + 1] += beams[row - 1][i]
            else:
                beams[row][i] += beams[row - 1][i]
    row += 1
for i in beams:
    print(i)
print(sum(beams[-1]))