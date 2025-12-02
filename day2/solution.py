with open('input.txt', 'r') as f:
    content = f.readlines()

content = content[0]
content = content.split(',')
for i in range(len(content)):
    content[i] = [int(x) for x in content[i].split('-')]

ans = 0
# Part 1
"""
for i in content:
    for j in range(i[0], i[1] + 1):
        temp = str(j)
        if len(temp) % 2 == 0 and temp[:len(temp) // 2] == temp[len(temp) // 2:len(temp)]:
            ans += j
print(ans)
"""
# Part 2
def is_invalid_id(id_value):
    s = str(id_value)

    # Try every possible block size that could repeat
    for size in range(1, len(s) // 2 + 1):
        if len(s) % size == 0:  # length must be divisible
            block = s[:size]
            if block * (len(s) // size) == s:
                return True

    return False

for i in content:
    for j in range(i[0], i[1] + 1):
        if is_invalid_id(j):
            ans += j
print(ans)