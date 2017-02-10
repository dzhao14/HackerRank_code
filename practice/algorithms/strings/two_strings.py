#https://www.hackerrank.com/domains/algorithms/strings/page:2

def solution(a, b):
    for i in a:
        if i in b:
            return "YES"
    return "NO"

if __name__ == "__main__":
    p = int(input())
    for i in range(p):
        a = input().strip()
        b = input().strip()
        ans = solution(a, b)
        print(ans)
