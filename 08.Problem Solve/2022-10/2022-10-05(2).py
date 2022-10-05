
def reverse(x: int):
    x = str(x)
    x = int(x[:: -1])

    return x


def isPrime(x: int):
    if x == 1:
        return False
    
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True


if __name__ == "__main__":
    n = int(input())
    nums= list(map(int, input().split()))

    for i in range(n):
        x = reverse(nums[i])
        if isPrime(x):
            print(x, end=' ')