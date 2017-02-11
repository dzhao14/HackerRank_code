#https://www.hackerrank.com/contests/rookierank-2/challenges/migratory-birds

def solution(arr):
    countr = [0 for i in range(6)]
    for i in arr:
        countr[i] += 1
    return countr.index(max(countr))

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
