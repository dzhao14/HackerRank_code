#https://www.hackerrank.com/challenges/kaprekar-numbers

import math

def solution(p, q):
    ans = []
    for i in range(p, q+1):
        rh = 0
        lh = 0
        s = pow(i,2)
        arr = [int(d) for d in str(s)]
        mid = math.floor(len(arr)/2)
        if arr[:mid]:
            lh = int(str(arr[:mid])[1:-1].replace(",","").replace(" ",""))
        if arr[mid:]:
            rh = int(str(arr[mid:])[1:-1].replace(",","").replace(" ",""))
        if rh and lh:
            if rh + lh == i:
                ans.append(i)
        else:
            if lh:
                if lh == i:
                    ans.append(i)
            if rh:
                if rh == i:
                    ans.append(i)
    return ans if ans else "INVALID RANGE"

if __name__ == "__main__":
    p = int(input())
    q = int(input())
    ans = solution(p, q)
    print("INVALID RANGE" if ans == "INVALID RANGE" else str(ans)[1:-1].replace(",",""))
