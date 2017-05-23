#https://www.hackerrank.com/contests/101hack49/challenges/calculate-array-size

import math

def solution(sizes):
    tot = sizes[0]
    for i in range(1, len(sizes)):
        tot = tot * sizes[i]
    return math.floor(tot * 4 / 1024)

if __name__ == "__main__":
    n = int(input())
    sizes = [int(_) for _ in input().strip().split()]
    ans = solution(sizes)
    print(str(ans))
