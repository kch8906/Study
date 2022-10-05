import sys
sys.stdin=open("2022-10/input.txt", "r")

n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size=len(s)
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print(f'#{i +  1} NO')
            break
    else:
        print(f'#{i + 1} YES')
