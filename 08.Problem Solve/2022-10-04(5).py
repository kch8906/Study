from typing import Counter


n, m = map(int, input().split())
count_list = [0] * (n * m)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_dice = i + j
        count_list[sum_dice] += 1

for idx, val in enumerate(count_list):
    if max(count_list) == val:
        print(idx, end=' ')


