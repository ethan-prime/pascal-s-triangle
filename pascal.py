row = int(input('enter row of pascal triangle (power+1): '))
term = int(input('input which term you would like (starts at 1): '))
result = []

for x in range(row):
    result.append([])
    for y in range(x+1):
        if x>1 and y != 0 and y<x:
            result[x].append(result[x-1][y-1] + result[x-1][y])
        else:
            result[x].append(1)

print(result[row-1][term-1])