#https://www.hackerrank.com/contests/w32/challenges/duplication

def calcS():
    s = '0'
    while len(s) < 1000:
        s = s + ''.join('1' if x == '0' else '0' for x in s)
    return s

if __name__ == "__main__":
    s = calcS()
    q = int(input())
    for i in range(q):
        idx = int(input())
        print(s[idx])
        
