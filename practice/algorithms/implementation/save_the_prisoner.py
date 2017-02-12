#https://www.hackerrank.com/challenges/save-the-prisoner

def solution(n, m, s):
    s = s - 1
    return ((s + m - 1) % n) + 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m, s = [int(t) for t in input().strip().split()]
        ans = solution(n, m, s)
        print(str(ans))
