for case in range(int(input())):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))

    extract_num = sorted(num[s - 1 : e])
    print(f'#{case + 1} {extract_num[k - 1]}')
