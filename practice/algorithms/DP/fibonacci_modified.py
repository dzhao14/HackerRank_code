#https://www.hackerrank.com/challenges/fibonacci-modified

def solution(f1, f2, n, memo):
    key = n
    if key in memo:
        return memo[key]
    if n == 1:
        return f1
    elif n == 2:
        return f2
    else:
        memo[key] = pow(solution(f1, f2, n-1, memo), 2) + solution(f1,f2, n-2, memo)
        return memo[key]
    

if __name__ == "__main__":
    f1, f2, n = [int(temp) for temp in input().strip().split()]
    ans = solution(f1, f2, n, {})
    print(str(ans))
