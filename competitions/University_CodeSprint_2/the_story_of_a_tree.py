#https://www.hackerrank.com/contests/university-codesprint-2/challenges/the-story-of-a-tree
#not solved

import queue
from fractions import Fraction

#Solutions 1 and two work but they're both O(n^2)

def solution(graph, parent, k, n):
    yes = 0
    
    for root in graph:
        count = 0
        seen = {}
        worklist = queue.Queue()
        worklist.put(root)
        while worklist.qsize() != 0:
            node = worklist.get()
            if node in seen:
                continue
            seen[node] = True
            if node in parent:
                for v in parent[node]:
                    if v not in seen:
                        count += 1
            for neib in graph[node]:
                worklist.put(neib)
        if count >= k:
            yes += 1

    ans = Fraction(yes, n)
    return str(ans.numerator) + "/" + str(ans.denominator)

def BFS_help(graph, v, u, roots):
    seen = {}
    seen[u] = True
    worklist = queue.Queue()
    worklist.put(v)
    while worklist.qsize() != 0:
        node = worklist.get()
        if node in seen:
            continue
        seen[node] = True
        roots[node-1] -= 1
        for neib in graph[node]:
            worklist.put(neib)

def solution2(graph, parent, k, n, g):
    yes = 0

    roots = [g for i in range(n)]
    #print(roots)

    seen = {}
    worklist = queue.Queue()
    worklist.put(1)
    while worklist.qsize() != 0:
        node = worklist.get()
        if node in seen:
            continue
        #seen[node] = True
        if node in parent:
            for v in parent[node]:
                BFS_help(graph, v, node, roots)
                    
        seen[node] = True    
        for neib in graph[node]:
            worklist.put(neib)

    for i in roots:
        if i >= k:
            yes += 1
    
    ans = Fraction(yes, n)
    print(roots)
    return str(ans.numerator) + "/" + str(ans.denominator)


def solution3(graph, parent, n, k, g, memo):
    memo = DP(graph, 1, n, k, g, memo)
    roots = [k for i in range(n)]
    for u in parent:
        roots[u-1] 

def DP(graph, start, n, k, g, memo):
    for neib in graph[start]:
        count = 1
        key = (start, neib)
        if key in memo:
            continue
        print(neib)
        memo[key] = sibling(graph, neib, start, memo)
        count += memo[key]
    return memo

def sibling(graph, neib, prev, memo):
    count = 1
    if len(graph[neib]) == 1:
        return count
    for neib2 in graph[neib]:
        key = (neib, neib2)
        if neib2 == prev:
            continue
        memo[key] = sibling(graph, neib2, neib, memo)
        count += memo[key]
    return count
    
    

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        parent = {}
        child = {}
        graph = {}
        n = int(input())
        for j in range(n-1):
            u, v = [int(t) for t in input().split()]
            
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]
        
        g, k = [int(t) for t in input().split()]
        for j in range(g):
            u, v = [int(t) for t in input().split()]
            if u in parent:
                parent[u].append(v)
            else:
                parent[u] = [v]
##            if v in child:
##                child[v].append(u)
##            else:
##                child[v] = [u]
        memo = {}
        print(graph)
        ans = solution3(graph, 1, n, k, g, memo)
        print(ans)

        
