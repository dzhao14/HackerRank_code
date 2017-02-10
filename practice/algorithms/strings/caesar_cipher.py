#https://www.hackerrank.com/challenges/caesar-cipher-1

def solution(s, k):
    out = ""
    for i in s:
        if 65 <= ord(i) <= 90:
            l = chr(((ord(i) - 65 + k) % 26) + 65)
            out = out + l
        elif 97 <= ord(i) <= 122:
            l = chr(((ord(i) - 97 + k) % 26) + 97)
            out = out + l
        else:
            out = out + i
    return out

if __name__ == "__main__":
    size = int(input())
    s = input().strip()
    k = int(input())
    ans = solution(s, k)
    print(ans)
