#https://www.hackerrank.com/challenges/anagram

def solution(s):
    if len(s) % 2 == 1:
        return -1
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    ar = [0 for i in range(26)]
    br = [0 for i in range(26)]
    for i in a:
        ar[ord(i)-97] += 1
    for i in b:
        br[ord(i)-97] += 1
    count = 0
    for i in range(26):
        count += abs(ar[i] - br[i])
    return count // 2

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        ans = solution(s)
        print(str(ans))
