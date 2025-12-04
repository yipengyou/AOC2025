with open('input.txt', 'r') as f:
    content = f.readlines()

banks = []
for i in content:
    banks.append([int(x) for x in i.strip()])

# Part 1
"""
ans = 0
for bank in banks:
    first = max(bank[:-1])
    firstindex = bank.index(first)
    second = max(bank[firstindex+1:])
    temp = int(str(first) + str(second))
    ans += temp
print(ans)
"""


# Part 2
ans = 0
for bank in banks:
    temp = ''
    for i in range(12):
        num = max(bank[:len(bank) - 11 + i])
        #print(bank[:len(bank) -11 + i])
        bank = bank[bank.index(num) + 1:]
        temp += str(num)
    #print(temp)
    ans += int(temp)
print(ans)