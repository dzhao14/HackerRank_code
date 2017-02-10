#https://www.hackerrank.com/challenges/unbounded-knapsack

import sys
sys.setrecursionlimit(5000)

def solution(arr, k, idx, tot, memo):
    key = (idx, tot)
    if key in memo:
        return memo[key]
    if idx >= len(arr):
        return -1 if tot > k else tot
    if tot > k:
        return -1
    else:
        memo[key] = max(solution(arr, k, idx, tot+arr[idx], memo),
                        solution(arr, k, idx+1, tot, memo),
                        tot)
        return memo[key]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = [int(temp) for temp in input().strip().split()]
        arr = [int(temp) for temp in input().strip().split()]
        ans = solution(arr, k, 0, 0, {})
        print(str(ans))
