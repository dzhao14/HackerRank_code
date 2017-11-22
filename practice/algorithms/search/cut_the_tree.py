#https://www.hackerrank.com/challenges/cut-the-tree/problem

import sys
sys.setrecursionlimit(10000000)

def calcSums(start, graph, values, n, best, parent):
    val = values[start]
    for neib in graph[start]:
        if parent[start] != neib:
            parent[neib] = start
            val += calcSums(neib, graph, values, n, best, parent)
    best[start] = val
    return val

def solution(graph, values, n):
    best = [0 for i in range(n)]
    parent = {}
    parent[0] = -1
    calcSums(0, graph, values, n, best, parent)
    
    minn = None
    for i in range(1, n):
        if minn == None:
            minn = abs((best[0] - best[i]) - best[i])
        else:
            minn = min(minn, abs((best[0] - best[i]) - best[i]))
    return minn

if __name__ == "__main__":
    n = int(input())
    values = [int(_) for _ in input().strip().split()]
    graph = {i : [] for i in range(n)}
    for i in range(n-1):
        u, v = [int(_) for _ in input().strip().split()]
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    ans = solution(graph, values, n)
    print(ans)
