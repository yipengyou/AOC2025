from math import prod
with open("input.txt", 'r') as f:
    content = f.readlines()
    
homework = [i.split() for i in content]

operations = homework.pop(-1)
fixed = [[] for i in homework[0]]

# Part 1
""""
for i in homework:
    for j in range(len(i)):
        fixed[j].append(i[j])
#print(operations)
ans = 0
for i, j in enumerate(fixed):
    if operations[i] == "+":
        ans += sum([int(x) for x in j])
    else:
        ans += prod([int(x) for x in j])
print(ans)
"""

# Part 2
for i in homework:
    for j in range(len(i)):
        fixed[j].append(i[j])
#print(operations)
ans = 0
for i, j in enumerate(fixed):
    if operations[i] == "+":
        ans += sum([int(x) for x in j])
    else:
        ans += prod([int(x) for x in j])
print(fixed, homework)