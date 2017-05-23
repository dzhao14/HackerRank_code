#https://www.hackerrank.com/contests/101hack49/challenges/summing-the-path-weights-between-nodes

import sys
sys.setrecursionlimit(10000000)

def DFS(node, graph, color, seen, tot, path_len):
    seen[node] = 1
    for neib in graph[node]:
        if seen[neib[0]] != 1:
            if color[neib[0]-1] == 1:
                tot += path_len + neib[1]
            tot = DFS(neib[0], graph, color, seen, tot, path_len + neib[1])
    return tot

def solution(graph, color, n):
    tot = 0
    for node in range(n):
        if color[node] == 0:
            seen = [0 for _ in range(n+1)]
            tot = DFS(node+1, graph, color, seen, tot, 0)
    return tot

if __name__ == "__main__":
    n = int(input())
    graph = {}
    color = [int(_) for _ in input().strip().split()] # 0 is red 1 is black
    for i in range(n-1):
        u, v, w = [int(_) for _ in input().strip().split()]
        if u not in graph:
            graph[u] = [(v,w)]
        else:
            graph[u].append((v, w))
        if v not in graph:
            graph[v] = [(u,w)]
        else:
            graph[v].append((u,w))
    ans = solution(graph, color, n)
    print(str(ans))
