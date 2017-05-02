#https://www.hackerrank.com/contests/hourrank-20/challenges/p-string

memo = []

def solution(s):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in s:
        if i == "a":
            a += 1
        elif i == "b":
            b += 1
        elif i == "c":
            c += 1
        else:
            d += 1
            
    for i in range(a+1):
        memo.append([])
        for j in range(b+1):
            memo[i].append([])
            for k in range(c+1):
                memo[i][j].append([])
                for l in range(d+1):
                    memo[i][j][k].append(0)
    return dp(a,b,c,d, memo)

def dp(w, x, y, z, memo):
    print(w,x,y,z)
    if w == 0 and x == 0 and y == 0 and z == 0:
        return 0
    if memo[w][x][y][z] == 1:
        return 0
    else:
        memo[w][x][y][z] == 1
        return w * dp(max(w-1,0), x, y, z, memo) + x * dp(w, max(x-1,0), y, z, memo) + y * dp(w, x, max(y-1,0), z, memo) + z * dp(w, x, y, max(z-1,0))

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        memo = []
        s = input().strip()
        ans = solution(s)
        print(str(ans))
