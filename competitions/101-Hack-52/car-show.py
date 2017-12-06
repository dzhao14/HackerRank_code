#https://www.hackerrank.com/contests/101hack52/challenges/car-show

import sys
A = 1000001

if __name__ == "__main__":
    n, q = [int(_) for _ in input().strip().split()]
    models = [int(_) for _ in input().strip().split()]
    fur = [0 for i in range(n)]
    seen = [-1 for i in range(A)]
    s = 0
    f = 0
    while s<n:
        if f<n and seen[models[f]] == -1:
            fur[s] = f-s+1
            seen[models[f]] = f
            f += 1
        elif f<n and seen[models[f]] != -1:
            seen[models[s]] = -1
            s += 1
            while s <= seen[models[f]]:
                fur[s] = fur[s-1] -1
                seen[models[s]] = -1
                s += 1
            seen[models[f]] = f
            fur[s] = f-s+1
            f += 1
        elif f == n and s+1 != n:
            fur[s+1] = fur[s]-1
            s += 1
        else:
            s += 1

    for i in range(q):
        l, r = [int(_) for _ in input().split()]
        total = 0
        for j in range(l-1, r):
            total += min(fur[j], r-j)
        print(total)
