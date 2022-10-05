import sys
sys.stdin = open('2022-10/input.txt', 'r')

n = int(input())
f_list = list(map(int, input().split()))
m = int(input())
s_list = list(map(int, input().split()))

p1 = p2 = 0
ch = []
maxnum = -2147000000

while p1 < n and p2 < m:
    if f_list[p1] <= s_list[p2]:
        ch.append(f_list[p1])
        p1 += 1
    else:
        ch.append(s_list[p2])
        p2 += 1

if p1 < n:
    ch = ch + f_list[p1:]
if p2 < m:
    ch = ch + s_list[p2:]

for i in ch:
    print(i, end=' ')