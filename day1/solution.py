with open('input.txt', 'r') as f:
    content = f.readlines()
    
"""
# Part 1
counter : int = 50
ans : int = 0
for line in content:
    if line[0] == "L":
        counter -= int(line[1:])
    else:
        counter += int(line[1:])
    counter = counter % 100
    if counter == 0:
        ans += 1
print(ans)
"""

# Part 2
counter : int = 50
ans : int = 0
for line in content:
    amount = int(line[1:])
    ans += amount // 100
    amount = amount % 100
    if line[0] == "L":
        if counter - amount < 0 and counter != 0:
            ans += 1
        counter -= amount
    else:
        if counter + amount > 100 and counter != 100:
            ans += 1
        counter += amount
        
    counter = counter % 100
    if counter == 0:
        ans += 1
    print(counter, ans)
