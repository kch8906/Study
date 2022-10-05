import sys

sys.stdin=open("2022-10/input.txt", "rt")
n = int(input())
result = list(map(int, input().split()))
ch = [0] * (n + 1)
cnt = 0

for i in range(n):
    if result[i] == 1:
        cnt += 1
        ch[i] = cnt
    else:
        cnt = 0

print(sum(ch))


