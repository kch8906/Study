import sys
sys.stdin = open('2022-10/input.txt', 'r')

n = int(input())
grids = [list(map(int, input().split())) for _ in range(n)]
max_score = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n): 
        sum1 += grids[i][j]
        sum2 += grids[j][i]

    if sum1 > max_score:
        max_score = sum1
    if sum2 > max_score:
        max_score = sum2

sum1 = sum2 = 0

for i in range(n):
    sum1 += grids[i][i]
    sum2 += grids[i][n -i - 1]
    
if sum1 > max_score:
    max_score = sum1
if sum2 > max_score:
    max_score = sum2

print(max_score)