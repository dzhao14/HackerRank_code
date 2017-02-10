#https://www.hackerrank.com/challenges/beautiful-binary-string

def solution(s):
    count = 0
    n = s.find("010")
    while n != -1:
        s = s[:n+2] + '1' + s[n+3:]
        count += 1
        n = s.find("010")
    return count

if __name__ == "__main__":
    size = int(input())
    s = input().strip()
    ans = solution(s)
    print(str(ans))
