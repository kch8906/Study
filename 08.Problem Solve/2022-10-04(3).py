n, k = map(int, input().split())
num = list(map(int, input().split()))
sum_list = []

for i in range(n):
    for j in range(i + 1, n):
        for q in range(j + 1, n):
            res = num[i] + num[j] + num[q]
            sum_list.append(res)

sum_list = sorted(sum_list, reverse=True)
print(sum_list[k - 1])
