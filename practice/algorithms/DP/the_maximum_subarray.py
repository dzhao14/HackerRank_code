#https://www.hackerrank.com/challenges/maxsubarray

def solutionBU(arr, memo):
    memo[len(arr)] = -10000
    done = -10000
    for i in range(len(arr)-1,-1,-1):
        memo[i] = max(memo[i+1] + arr[i], arr[i])
        if memo[i+1] > done:
            done = memo[i+1]
    return max(memo[0], done)

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

def solution2BU(arr, memo):
    memo[len(arr)] = -10000
    for i in range(len(arr)-1,-1,-1):
        memo[i] = max(memo[i+1] + arr[i], arr[i], memo[i+1])
    return memo[0]

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
        ans1 = solutionBU(arr, memo)
        ans2 = solution2BU(arr, memo2)
        ans = (ans1, ans2)
        print(str(ans)[1:-1].replace(",",""))
        
