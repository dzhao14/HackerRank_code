#https://www.hackerrank.com/contests/rookierank-3/challenges/maximal-tourism

import sys
sys.setrecursionlimit(100000)

def solution(edges):
    cs = [0 for _ in range(n)]
    count = -1
    for i in range(len(cs)):
        if cs[i] == 0:
            cs[i] = 1
            count = max(count, dfs(i, edges, cs))
    return count

def dfs(start, edges, seen):
    count = 1
    for neib in edges[start+1]:
        if seen[neib-1] == 0:
            seen[neib-1] = 1
            count += dfs(neib-1, edges, seen)
    return count

if __name__ == "__main__":
    edges = {}
    nm = [int(_) for _ in input().strip().split()]
    n = nm[0]
    m = nm[1]
    for i in range(n):
        edges[i+1] = []
    for i in range(m):
        uv = [int(_) for _ in input().strip().split()]
        u = uv[0]
        v = uv[1]
        edges[u].append(v)
        edges[v].append(u)
    ans = solution(edges)
    print(str(ans))
