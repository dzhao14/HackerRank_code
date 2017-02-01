#https://www.hackerrank.com/contests/world-codesprint-9/challenges/kingdom-division

#not solved

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

#return the degree of this node 
def degree(n, graph):
    return len(graph[n])

#returns the number of nodes with degree > 1 not seen in the graph
#including this one
def unseenNodes(n, graph, seen, nodes):
    myself = 0
    if degree(n, graph) != 1:
        myself = 1
        nodes[n] = graph[n]
    neibs = 0
    for neib in graph[n]:
        if neib in seen:
            continue
        elif degree(neib, graph) == 1:
            continue
        else:
            newseen = {}
            newseen[neib] = True
            newseen[n] = True
            neibs += unseenNodes(neib, graph, newseen, nodes)
    
    return myself + neibs   

def blocks(blocker_deg, cut_size):
    return zero(cut_size - (blocker_deg - 1))

def zero(n):
    if n < 0:
        return 0
    return n

def degNoLeaf(n, graph):
    num = 0
    for neib in graph[n]:
        if degree(neib, graph) == 1:
            continue
        else:
            num += 1
    return num

def sub_blockers(middleN, nodes, graph):
    res = 0
    edges = middleN - 1
    blockers = []
    for x in range(edges + 1):
        blockers.append(0)
    for node in nodes:
        deg = degNoLeaf(node, graph)
        if deg == 1:
            continue
        for x in range(2, edges):
            blockval = blocks(deg, x)
            blockers[x] += blockval
    for x in range(edges):
        res += zero(ncr(edges,x) - blockers[x])
    return res
            

        
if __name__ == "__main__":
    graph = {}
    size_graph = int(input())
    weird = 0
    for i in range(1, size_graph):
        edge = input()
        edge = edge.split()
        u = int(edge[0])
        v = int(edge[1])
        if u not in graph:
            graph[u] = []
            graph[u] = [v]
        else:
            graph[u] = graph[u] + [v]

        if v not in graph:
            graph[v] = []
            graph[v] = [u]
        else:
            graph[v] = graph[v] + [u]
        for key in graph:
            if degree(key, graph) == 1:
                weird = key
                break
    nodes = {}
    middleN = unseenNodes(weird, graph, {}, nodes)
    if middleN == 0:
        print(2)
    else:
        ans = 2 * sub_blockers(middleN, nodes, graph)
        ans = ans % (pow(10,9) + 7)
        print(ans)
