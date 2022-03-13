data = input().upper()
data_list = []
for i in range(int(input())):
    word = input().upper()
    result = []
    for j in data:
        cnt = 0
        for k in word:
            if j == k:
                result.append(cnt)
                break
            else:
                cnt += 1

    if min(result) == result[0] and max(result) == result[2]:
        print('#{} YES'.format(i + 1))
    else:
        print('#{} NO'.format(i + 1))
