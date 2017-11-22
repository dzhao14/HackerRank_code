#https://www.hackerrank.com/challenges/richie-rich/problem

def solution(ss, k):
    s = [i for i in ss]
    start = len(s) // 2
    changed = {}
    
    while start < len(s):
        if s[start] != s[-start-1]:
            if s[start] > s[-start-1]:
                s[-start-1] = s[start]
            else:
                s[start] = s[-start-1]
            k -= 1
            changed[start] = True
            changed[-start-1] = True
        start += 1

    if k < 0:
        return -1

    maximize = len(s)-1
    while k > 0 and maximize >= len(s) // 2:
        if s[maximize] != 9 and maximize in changed:
            s[maximize] = 9
            s[-maximize-1] = 9
            k -= 1
        elif s[maximize] != 9 and k >= 2:
            s[maximize] = 9
            s[-maximize-1] = 9
            k -= 2
        else:
            pass
        maximize -= 1

    if k > 0 and len(s) % 2 == 1:
        s[len(s) // 2] = 9
    
    ans = ""
    for i in range(len(s)):
        ans += str(s[i])
    return ans


if __name__ == "__main__":
    n, k = [int(_) for _ in input().strip().split()]
    s = input().strip()
    ss = [int(i) for i in s]
    ans = solution(ss, k)
    print(ans)

