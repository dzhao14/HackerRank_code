#https://www.hackerrank.com/contests/university-codesprint-3/challenges/black-white-tree

import queue

def root(edges):
    #lets start at node 0. Why not?

    parents = {}
    parents[0] = -1
    unseen = queue.Queue()
    order = []
    unseen.put(0)
    while unseen.qsize() > 0:
        at = unseen.get()
        order.append(at)
        for neib in edges[at]:
            if parents[at] != neib:
                unseen.put(neib)
                parents[neib] = at

    return order, parents

def isBlack(node, colors):
    if colors[node] == 1:
        return 1
    else:
        return -1

def isWhite(node, colors):
    if colors[node] == 0:
        return 1
    else:
        return -1

def getAnswer(node, amount, edges, parents):
    num_nodes = 0
    ans_nodes = []
    toSearch = queue.Queue()
    toSearch.put(node)

    while toSearch.qsize() > 0:
        at = toSearch.get()
        num_nodes += 1
        ans_nodes.append(at)
        for neib in edges[at]:
            if parents[neib] == at and amount[neib] > 0:
                toSearch.put(neib)
    ans_nodes = [i+1 for i in ans_nodes]
    return num_nodes, ans_nodes

def solution(n, colors, edges):
    order, parents = root(edges)
    amountBlack = [-2 for i in range(n)]
    amountWhite = [-2 for i in range(n)]
    max_disparity = 0
    for node in reversed(order):
        amountBlack[node] = max(0, (isBlack(node, colors) +
                             sum([amountBlack[neib] for neib in edges[node] if amountBlack[neib] != -2])))
        amountWhite[node] = max(0, (isWhite(node, colors) +
                             sum([amountWhite[neib] for neib in edges[node] if amountWhite[neib] != -2])))
    strangeness = max(max(amountWhite), max(amountBlack))

    try:
        idx = amountBlack.index(strangeness)
        num_nodes, ans_nodes = getAnswer(idx, amountBlack, edges, parents)
    except:
        idx = amountWhite.index(strangeness)
        num_nodes, ans_nodes = getAnswer(idx, amountWhite, edges, parents)
    print(strangeness)
    print(num_nodes)
    print(str(ans_nodes)[1:-1].replace(',', ''))



if __name__ == "__main__":
    n = int(input().strip())
    colors = [int(_) for _ in input().strip().split()]
    edges = {i : [] for i in range(n)}
    for i in range(n-1):
        x, y = [int(_) for _ in input().strip().split()]
        edges[x-1].append(y-1)
        edges[y-1].append(x-1)
    solution(n, colors, edges)
    
