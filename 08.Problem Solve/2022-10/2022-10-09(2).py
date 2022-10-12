import sys
sys.stdin = open('2022-10/input.txt', 'r')

n = int(input())
grids = [list(map(int, input().split())) for _ in range(n)]

s = e = n // 2
result = 0

for i in range(n):
    for j in range(s, e + 1):
        result += grids[i][j]

    if i < (n // 2):
        s -= 1
        e += 1

    else:
        s += 1
        e -= 1

print(result)