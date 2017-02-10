#https://www.hackerrank.com/challenges/alternating-characters

def solution(s):
    prev = s[0]
    count = 0
    for i in s[1:]:
        if i == prev:
            count += 1
        else:
            prev = i
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        ans = solution(s)
        print(str(ans))
