#https://www.hackerrank.com/contests/101hack47/challenges/modular-game-of-numbers

def solution(n, p, q):
    sums = [0 for _ in range(n)]
    counts = [0 for _ in range(n+1)]
    for i in p:
        for j in q:
            sums[(i+j)%n] += 1
    minimum = min(sums)
    ans = []
    for i in range(n):
        if sums[i] == minimum:
            for j in range(1, n+1):
                if (j + i) % n == 0:
                    ans.append(j)
    return min(ans)
    

        

if __name__ == "__main__":
    n, ps, qs = [int(_) for _ in input().strip().split()]
    p = [int(_) for _ in input().strip().split()]
    q = [int(_) for _ in input().strip().split()]

    ans = solution(n, p, q)
    print(str(ans))
    
