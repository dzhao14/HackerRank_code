#https://www.hackerrank.com/contests/rookierank-2/challenges/hackerrank-in-a-string

def contains(s, l, idx):
    try:
        return s[idx:].index(l) + idx
    except:
        return -1

def solution(s):
    idx = 0
    hackerrank = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    for i in hackerrank:
        idx = contains(s, i, idx)
        if idx == -1:
            return "NO"
        idx = idx + 1
    return "YES"
    

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        s = input().strip()
        ans = solution(s)
        print(ans)
