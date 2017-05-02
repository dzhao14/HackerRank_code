#https://www.hackerrank.com/contests/hourrank-20/challenges/hot-and-cold

def solution(arr):
    if min(arr[2], arr[3]) -  max(arr[0], arr[1]) < 0:
        return "NO"
    return "YES"

if __name__ == "__main__":
    arr = [int(_) for _ in input().strip().split()]
    ans = solution(arr)
    print(ans)
