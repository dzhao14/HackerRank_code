#https://www.hackerrank.com/challenges/extra-long-factorials

def solution(n):
    ans = 1
    for i in range(2, n+1):
        ans = ans * i
    return ans

if __name__ == "__main__":
    n = int(input())
    ans = solution(n)
    print(str(ans))
