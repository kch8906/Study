n = int(input())
scores = list(map(int, input().split()))
mean_score = int(round(sum(scores) / n, 0))
min = 214700000

for idx, val in enumerate(scores):
    tmp = abs(val - mean_score)
    if tmp < min:
        min = tmp
        score = val
        res = idx + 1
    elif tmp == min:
        if val > score:
            score = val
            res = idx + 1

print(mean_score, res)