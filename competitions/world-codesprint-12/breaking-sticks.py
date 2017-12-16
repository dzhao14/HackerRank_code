#https://www.hackerrank.com/contests/world-codesprint-12/challenges/breaking-sticks/problem

import math

def pf(n):
    """Return a list containing the primes whose product equals n"""
    assert n > 0
    if n == 1:
        return []
    ans = []
    d = 2
    m = 2
    cutoff = int(math.sqrt(n))
    while n>1:
        if d > cutoff:
            ans.append(int(n))
            break
        if n%d == 0:
            ans.append(d)
            n = n/d
            cutoff = int(math.sqrt(n))
        else:
            if d > 3:
                if m == 0 or m == 4:
                    d += 1
                    m += 1
                elif m == 2:
                    d += 3
                    m += 3
                elif m == 3 or m == 5:
                    d += 2
                    m += 2
                else:
                    d += 4
                    m += 4
                if m > 5:
                    m -= 6
            else:
                d += 1
                m += 1
    
    return ans

def solution(sticks):
    ans = sum(sticks) + len(sticks) 
    for stick in sticks:
        if stick == 1:
            ans -= 1
        pfs = pf(stick)
        counter = 1
        for p in range(len(pfs)-1, 0, -1):
            counter *= pfs[p]
            ans += counter

    return ans

if __name__ == "__main__":
    n = int(input())
    sticks = [int(_) for _ in input().strip().split()]
    ans = solution(sticks)
    print(ans)
