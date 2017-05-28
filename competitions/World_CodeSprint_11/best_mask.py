#https://www.hackerrank.com/contests/world-codesprint-11/challenges/best-mask

def solution(arr):
    x = 0
    arr.sort()
    for a in arr:
        if x & a != 0:
            continue
        else:
            temp = 0
            while (1 << temp) & a == 0:
                temp += 1
            x = x | (1 << temp)
    return x

if __name__ == "__main__":
    n = int(input())
    arr = [int(_) for _ in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
