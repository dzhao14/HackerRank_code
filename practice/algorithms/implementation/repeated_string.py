#https://www.hackerrank.com/challenges/repeated-string

def solution(s, n):
    count = 0
    l = len(s)
    a = 0
    for i in s:
        if i == 'a':
            a += 1
    whole = n // l
    count = whole * a
    if n % l == 0:
        return count
    remain = n - (whole * l)
    for i in range(remain):
        if s[i] == 'a':
            count += 1
    return count
        

if __name__ == "__main__":
    s = input().strip()
    n = int(input())
    ans = solution(s, n)
    print(str(ans))
