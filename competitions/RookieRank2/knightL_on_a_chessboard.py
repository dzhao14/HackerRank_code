#https://www.hackerrank.com/contests/rookierank-2/challenges/knightl-on-chessboard

import queue

def validNode(n, node):
    if node[0] >= n or node[0] < 0:
        return False
    if node[1] >= n or node[1] < 0:
        return False
    return True

def calcNeibs(n, node, a, b):
    x = node[0]
    y = node[1]
    neibs = []
    neibs.append((x+a, y+b))
    neibs.append((x+a, y-b))
    neibs.append((x-a, y+b))
    neibs.append((x-a, y-b))
    neibs.append((x+b, y+a))
    neibs.append((x+b, y-a))
    neibs.append((x-b, y+a))
    neibs.append((x-b, y-a))
    return neibs

def BFS(n, a, b):
    seen = {}
    parent = {}
    worklist = queue.Queue()
    worklist.put((0,0))
    while worklist.qsize() != 0:
        node = worklist.get()
        if node in seen:
            continue
        seen[node] = True
        for neib in calcNeibs(n, node, a, b):
            if validNode(n, neib) and neib not in seen:
                worklist.put(neib)
                parent[neib] = node
            else:
                continue
    if (n-1, n-1) in seen:
        ans = retrace(n, parent)
        return ans
    else:
        return -1

def retrace(n, parent):
    count = 0
    node = (n-1, n-1)
    while node in parent:
        p = parent[node]
        count += 1
        if p == (0,0):
            return count
        else:
            node = p

def solution(n, a, solved):
    ans = []
    for b in range(1, n):
        if (a, b) in solved:
            ans.append(solved[(a,b)])
        elif (b, a) in solved:
            ans.append(solved[(b, a)])
        else:
            dis = (BFS(n, a, b))
            solved[(a, b)] = dis
            ans.append(dis)
    return ans
        

if __name__ == "__main__":
    n = int(input())
    solved = {}
    for i in range(1, n):
        ans = solution(n, i, solved)
        print(str(ans)[1:-1].replace(",",""))
    
