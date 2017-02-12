#https://www.hackerrank.com/challenges/flatland-space-stations

import math
def solution(arr, n):
    md = arr[0]
    last = arr[0]
    for i in arr[1:]:
        md = max(md, (i - last)//2)
        last = i
    md = max(md, n - arr[-1]-1)
    return md

if __name__ =="__main__":
    n, m = [int(t) for t in input().strip().split()]
    arrm = [int(t) for t in input().strip().split()]
    arr = sorted(arrm)
    ans = solution(arr, n)
    print(str(ans))
