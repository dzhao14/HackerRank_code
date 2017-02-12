#https://www.hackerrank.com/challenges/strange-code

import math

def solution(t):
    if t <= 3:
        return 3-(t-1)
    tot = {}
    tot[1] = 3
    x = 1
    while tot[x] < t:
        x+=1
        tot[x] = tot[x-1] + pow(2, x) + pow(2,x-1)

    rem = t - tot[x-1]-1
    return pow(2,x) + pow(2,x-1) - rem

if __name__ == "__main__":
    t = int(input())
    ans = solution(t)
    print(str(ans))
