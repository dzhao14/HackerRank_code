#https://www.hackerrank.com/challenges/sherlock-and-squares

import math
def solution(a, b):
    count = 0
    low = math.floor(math.sqrt(a))
    hi = math.floor(math.sqrt(b))
    for i in range(low, hi+1):
        p = pow(i, 2)
        if p >= a and p <= b:
            count += 1
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = [int(d) for d in input().strip().split()]
        ans = solution(a, b)
        print(str(ans))
