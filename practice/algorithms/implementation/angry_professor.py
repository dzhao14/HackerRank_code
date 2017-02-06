#https://www.hackerrank.com/challenges/angry-professor

def solution(k, arr):
    count = 0
    for i in arr:
        if i <= 0:
            count += 1
    return "NO" if count >= k else "YES"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = [int(temp) for temp in input().strip().split()]
        arr = [int(temp) for temp in input().strip().split()]
        ans = solution(k, arr)
        print(ans)
