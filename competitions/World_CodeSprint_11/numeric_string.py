#https://www.hackerrank.com/contests/world-codesprint-11/challenges/numeric-string

import math

def solution(s, k, b, m):
    memo = {}
    ans = 0
    for i in range(len(s) - k + 1):
        sub = s[i:i+k]
        if sub in memo:
            ans += memo[sub]
        else:
            base_b = int(sub, b)
            mod = base_b % m
            ans += mod
            memo[sub] = mod
    return ans

def solution2(s, k, b, m):
    ans = 0
    first = 0 
    start = int(s[:k], b)
    ans += start % m
    for i in range(k, len(s)):
        start = ((start - (int(s[first]) * pow(b, k-1))) * b) + int(s[i])
        ans += start % m
        first += 1
    return ans

def solution3(s, k, b, m):
    ans = 0
    first = 0
    shift = pow(b, k-1) % m
    start = int(s[:k], b) % m
    ans += start
    
    for i in range(k, len(s)):
        start = (start - ((int(s[first]) % m) * shift)) % m
        start = (start * b) % m
        start = (start + int(s[i])) % m
        ans += start
        first += 1
    return ans

if __name__ == "__main__":
    s = input().strip()
    k, b, m = [int(_) for _ in input().strip().split()]
    ans = solution3(s, k, b, m)
    print(str(ans))
    
