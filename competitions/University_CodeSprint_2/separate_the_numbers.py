#https://www.hackerrank.com/contests/university-codesprint-2/challenges/separate-the-numbers

def solution(s):
    for l in range(1,len(s)//2 + 1):
        no = False
        if int(s[0]) == 0:
            continue
        start = l
        size = l
        n = int(s[:l])
        while start < len(s):
            if int(s[start]) == 0:
                no = True
                break
            if n % pow(10,len(str(n))) == pow(10,len(str(n))) - 1:
                if int(s[start:start+size+1]) - n == 1:
                    n = int(s[start:start+size+1])
                    start = start + size + 1
                    size += 1
                else:
                    no = True
                    break
            elif int(s[start:start+size]) - n == 1:
                n = int(s[start:start+size])
                start = start + size
            else:
                no = True
                break
        if not no:
            return "YES " + s[:l]
    return "NO"
            

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        s = input().strip()
        ans = solution(s)
        print(ans)
