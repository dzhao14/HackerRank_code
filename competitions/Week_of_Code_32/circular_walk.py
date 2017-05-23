#https://www.hackerrank.com/contests/w32/challenges/circular-walk

import queue

def solution(s, t, n, R, best):
    if s == t:
        return 0
    wl = queue.Queue()
    wl.put(s)
    best[s] = 0
    while not wl.empty():
        i = wl.get()
        for j in range(-R[i], R[i] + 1):
            new = (i+j)%n
            if best[new] == n+1 and new != i:
                wl.put(new)
                best[new] = min(best[new], best[i] + 1)
    return -1 if best[t] == n+1 else best[t]
        
    

def calcR(ro, n, g, seed, p):
    R = [0 for i in range(n)]
    R[0] = ro
    for i in range(1, n):
        R[i] = (R[i-1] % p * g % p + seed % p) % p
    
    return R

if __name__ == "__main__":
    n, s, t = [int(_) for _ in input().strip().split()]
    ro, g, seed, p = [int(_) for _ in input().strip().split()]
    R = calcR(ro, n, g, seed, p)
    best = [n+1 for i in range(n)]
    ans = solution(s, t, n, R, best)
    print(ans)
