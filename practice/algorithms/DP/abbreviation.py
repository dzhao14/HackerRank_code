#https://www.hackerrank.com/challenges/abbr

def solution(a, b, idxA, idxB, memo):
    key = (idxA, idxB)
    if key in memo:
        return memo[key]
    if idxA >= len(a) and idxB <= len(b)-1:
        return False
    if idxB >= len(b):
        if idxA >= len(a):
            memo[key] = True
            return memo[key]
        if 65 <= ord(a[idxA]) <=90:
            memo[key] = False
            return memo[key]
        else:
            memo[key] = solution(a, b, idxA+1, idxB, memo)
            return memo[key]
    else:
        if 65 <= ord(a[idxA]) <= 90:
            if a[idxA] == b[idxB]:
                memo[key] = solution(a, b, idxA+1, idxB+1, memo)
                return solution(a, b, idxA+1, idxB+1, memo)
            else:
                memo[key] = False
                return memo[key]
        else:
            if ord(a[idxA]) - 32 == ord(b[idxB]):
                memo[key] = (solution(a, b, idxA + 1, idxB+1, memo) or
                             solution(a, b, idxA+1, idxB, memo))
                return memo[key]
            else:
                memo[key] = solution(a, b, idxA+1, idxB, memo)
                return memo[key]

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        a = input().strip()
        b = input().strip()
        memo = {}
        ans = solution(a, b, 0, 0, memo)
        d = "YES" if ans else "NO"
        print(d)
