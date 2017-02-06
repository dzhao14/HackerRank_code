#https://www.hackerrank.com/challenges/funny-string

def solution(s, r):
    for i in range(len(s)-1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(r[i]) - ord(r[i+1])):
            return "Not Funny"
    return "Funny"


if __name__ == "__main__":
    num = int(input())
    for i in range(num):
        s = input().strip()
        r = s[::-1]
        ans = solution(s,r)
        print(ans)
                
