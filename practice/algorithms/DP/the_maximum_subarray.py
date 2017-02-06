#https://www.hackerrank.com/challenges/maxsubarray
#Not solved bc top-down method takes too many recursive calls

#TODO: Turn DP from top-down to bottom-up

def solution(arr, idx, tot, memo):
    key = (tot, idx)
    if key in memo:
        return memo[key]
    if idx >= len(arr):
        return tot
    else:
        memo[key] = max(solution(arr, idx+1, tot+arr[idx], memo),
                        solution(arr, idx+1, arr[idx], memo),
                        tot)
        return memo[key]

def solution2(arr, idx, TOT, memo):
    key = (TOT, idx)
    if key in memo:
        return memo[key]
    if idx >= len(arr):
        return TOT
    else:
        memo[key] = max(solution2(arr, idx+1, TOT+arr[idx], memo),
                        solution2(arr, idx+1, TOT, memo),
                        solution2(arr, idx+1, arr[idx], memo),
                        TOT)
        return memo[key]
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(temp) for temp in input().strip().split()]
        memo = {}
        memo2 = {}
        ans1 = solution(arr, 1, arr[0], memo)
        ans2 = solution2(arr, 1, arr[0], memo2)
        ans = (ans1, ans2)
        print(str(ans)[1:-1].replace(",",""))
        
