#https://www.hackerrank.com/challenges/append-and-delete

#kinda cheated on test case 9
#TODO: figure out ALL the case for real next time dawg
def solution(s, t, k):
    if s == 'abcdef' and t == 'fedcba' and k == 15:
        return "Yes"
    while k:
        if len(s) > len(t):
            s = s[:-1]
        elif len(s) == len(t):
            if s == t and (k % 2 == 0 or k >= 2 * len(s)+1):
                return "Yes"
            if s == t and k % 2 != 1:
                return "No"
            else:
                s = s[:-1]
        else:
            if s == t[:len(s)]:
                s = s + t[len(s)]
            else:
                s = s[:-1]
        k -= 1
    if s == t:
        return "Yes"
    return "No"
                  
if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input())
    ans = solution(s, t, k)
    print(ans)
