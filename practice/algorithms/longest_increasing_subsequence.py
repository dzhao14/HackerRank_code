#https://www.hackerrank.com/challenges/longest-increasing-subsequent
#not solved

import sys
sys.setrecursionlimit(10000000)

def solution(arr, prev, idx, tot, memo):
    key = (idx, prev, tot)
    if key in memo:
        return memo[key]
    if idx == len(arr):
        return tot
    if arr[idx] < prev:
        memo[key] = max(solution(arr, arr[idx], idx+1, 1, memo),
                        solution(arr, prev, idx+1, tot, memo))
        return memo[key]
    else:
        memo[key] = max(solution(arr, arr[idx], idx+1, tot+1, memo),
                        solution(arr, arr[idx], idx+1, 1, memo))
        return memo[key]

if __name__ == "__main__":
    size = int(input())
    arr = []
    for i in range(size):
        n = int(input())
        arr.append(n)
    memo = {}
    ans = solution(arr, arr[0], 1, 1, memo)
    print(str(ans))
