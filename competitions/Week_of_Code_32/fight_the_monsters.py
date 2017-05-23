#https://www.hackerrank.com/contests/w32/challenges/fight-the-monsters

import math

def solution(healths, hit, t):
    healths.sort()
    monster = 0
    count = 0
    while t > 0:
        if monster == len(healths):
            break;
        needed = math.ceil(healths[monster] / hit)
        if needed <= t:
            count += 1
            t -= needed
            monster += 1
        else:
            break
        
    return count

if __name__ == "__main__":
    n, hit, t = [int(_) for _ in input().strip().split()]
    healths = [int(_) for _ in input().strip().split()]
    ans = solution(healths, hit, t)
    print(str(ans))
