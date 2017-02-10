#https://www.hackerrank.com/challenges/string-construction

def solution(s):
    cost = 0
    for i in range(26):
        if chr(i+97) in s:
            cost += 1
    return cost
            

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        ans = solution(s)
        print(str(ans))
