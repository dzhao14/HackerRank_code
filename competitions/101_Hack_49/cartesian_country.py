#https://www.hackerrank.com/contests/101hack49/challenges/cartesian-country

import math

def solution(x1, y1, x2, y2, xc, yc):
    width = min(x2 - xc, xc - x1)
    height = min(y2 - yc, yc - y1)
    return math.floor(((width * 2 + 1) * (height * 2 + 1) - 1)/2)

if __name__ == "__main__":
    x1, y1 = [int(_) for _ in input().strip().split()]
    x2, y2 = [int(_) for _ in input().strip().split()]
    xc, yc = [int(_) for _ in input().strip().split()]
    ans = solution(x1, y1, x2, y2, xc, yc)
    print(str(ans))
