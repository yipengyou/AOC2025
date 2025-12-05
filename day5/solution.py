with open('input1.txt', 'r') as f:
    content1 = f.readlines()


# Part 1
"""
with open('input2.txt', 'r') as f:
    content2 = f.readlines()

isFresh = []
for i in content1:
    isFresh.append([int(x) for x in i.strip().split('-')])
isFresh.sort()

food = [int(i) for i in content2]

# clean up the overlapping ranges

merged = [isFresh[0]]

for start, end in isFresh[1:]:
    last_start, last_end = merged[-1]

    # Check overlap
    if start <= last_end:
        # Merge
        merged[-1] = (last_start, max(last_end, end))
    else:
        merged.append([start, end])

ans = 0
for i in food:
    for j in merged:
        if i >= j[0] and i <= j[1]:
            ans += 1

print(ans)
"""

# Part 2

isFresh = []
for i in content1:
    isFresh.append([int(x) for x in i.strip().split('-')])
isFresh.sort()

# clean up the overlapping ranges

merged = [isFresh[0]]

for start, end in isFresh[1:]:
    last_start, last_end = merged[-1]

    # Check overlap
    if start <= last_end:
        # Merge
        merged[-1] = (last_start, max(last_end, end))
    else:
        merged.append([start, end])

ans = 0

for i in merged:
    ans += i[1] - i[0] + 1

print(ans)