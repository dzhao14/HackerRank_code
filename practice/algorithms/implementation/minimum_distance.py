#https://www.hackerrank.com/challenges/minimum-distances

def solution(arr):
    prev = {}
    mindistance = 10000
    for i in range(len(arr)):
        if arr[i] in prev:
            dis = i - prev[arr[i]]
            mindistance = min(dis, mindistance)
        else:
            prev[arr[i]] = i
    if mindistance == 10000:
        return -1
    else:
        return mindistance

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
