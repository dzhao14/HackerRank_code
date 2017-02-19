#https://www.hackerrank.com/challenges/non-divisible-subset

import math

def onemax(n):
    if n > 1:
        return 1
    else:
        return n

def solution(arr, k):
    pair = {}
    countr = [0 for i in range(k)]
    for n in arr:
        countr[n%k] += 1
    count = 0
    for i in range(k//2 + 1):
        if (2*i) % k == 0:
            count += onemax(countr[i])
        else:
            count += max(countr[i], countr[-i])
    
    return count

if __name__ == "__main__":
    n, k = [int(t) for t in input().strip().split()]
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr, k)
    print(str(ans))
