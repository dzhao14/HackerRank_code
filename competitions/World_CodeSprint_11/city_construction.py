#https://www.hackerrank.com/contests/world-codesprint-11/challenges/hackerland

import sys
sys.setrecursionlimit(100000)

def DFS(graph, n, s, t):
    seen = [0 for i in range(n+1)]
    stack = [s]
    while len(stack) != 0:
        node = stack.pop()
        seen[node] = 1
        if node == t:
            return True
        for neib in graph[node]:
            if seen[neib] != 1:
                stack.append(neib)
    return False

def solution(graph, n, q):
    nn = n
    for i in range(q):
        s = input().strip().split()
        if int(s[0]) == 1:
            if int(s[2]) == 0:
                graph[int(s[1])].append(nn+1)
                graph[nn+1] = []
            else:
                graph[nn+1] = [int(s[1])]
            nn += 1
        else:
            if DFS(graph, nn, int(s[1]), int(s[2])):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    graph = {}
    n, m = [int(_) for _ in input().strip().split()]
    for i in range(1, n+1):
        graph[i] = []
    for i in range(m):
        u, v = [int(_) for _ in input().strip().split()]
        graph[u].append(v)
    q = int(input())
    solution(graph, n, q)
