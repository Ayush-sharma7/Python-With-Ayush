import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_triplets(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_prime(arr[i] * arr[j] * arr[k]):
                    count += 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(count_triplets(arr))
