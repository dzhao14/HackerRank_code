#https://www.hackerrank.com/challenges/the-love-letter-mystery

def solution(s):
    count = 0
    for i in range(len(s)//2):
        a = ord(s[i])
        b = ord(s[-i-1])
        count += abs(a-b)
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        ans = solution(s)
        print(str(ans))
