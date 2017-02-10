#https://www.hackerrank.com/challenges/game-of-thrones

def solution(s):
    arr = [0 for i in range(26)]
    for i in s:
        arr[ord(i) - 97] += 1
    odd = False
    for i in arr:
        if i % 2 == 1 and not odd:
            odd = True
        elif i % 2 == 1 and odd:
            return "NO"
    return "YES"
    
    

if __name__ == "__main__":
    s = input().strip()
    ans = solution(s)
    print(ans)
