def degit_sum(x):
    sum_x = 0
    for i in str(x):
        sum_x += int(i)

    return sum_x


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    max_num = -2147000000

    for i in range(len(nums)):
        res = degit_sum(nums[i])
        if res > max_num:
            max_num = res
            idx = i

    else:
        print(nums[idx])