#https://www.hackerrank.com/contests/rookierank-2/challenges/minimum-absolute-difference-in-an-array

def solution(arr):
    sr = sorted(arr)
    m = 3000000000
    for i in range(len(arr)-1):
        if abs(sr[i] - sr[i+1]) < m:
            m = abs(sr[i] - sr[i+1])
    return m

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
