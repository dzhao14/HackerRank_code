#https://www.hackerrank.com/contests/world-codesprint-11/challenges/balanced-array

def solution(arr):
    l = sum(arr[:int(len(arr)/2)])
    r = sum(arr[int(len(arr)/2):])
    return abs(l-r)

if __name__ == "__main__":
    n = int(input())
    arr = [int(_) for _ in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
