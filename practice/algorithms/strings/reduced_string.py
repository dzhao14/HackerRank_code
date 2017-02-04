#https://www.hackerrank.com/challenges/reduced-string

def solution(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            newS = s[:i]+s[i+2:]
            return solution(newS)
    if s:
        return s
    else:
        return "Empty String"

if __name__ == "__main__":
    s = input().strip()
    ans = solution(s)
    print(ans)
