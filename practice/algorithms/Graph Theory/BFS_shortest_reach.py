#https://www.hackerrank.com/challenges/bfsshortreach

import queue

def changeDis(dis, s, f):
    if dis[f-1] == -1 or dis[s-1] + 6 < dis[f-1]:
        dis[f-1] = dis[s-1] + 6
        

def solution(graph, start, size):
    dis = [-1 for i in range(size)]
    dis[start-1] = 0
    seen = {}
    worklist = queue.Queue()
    worklist.put(start)
    while worklist.qsize() != 0:
        node = worklist.get()
        if node in seen:
            continue
        seen[node] = True
        for neib in graph[node]:
            if neib in seen:
                continue
            else:
                worklist.put(neib)
                changeDis(dis, node, neib)
    del dis[start-1]
    return dis
        
    
    

if __name__ == "__main__":
    q = int(input())
    for i in range (q):
        graph = {}
        nodes, edges = [int(temp) for temp in input().strip().split()]
        for n in range(1,nodes+1):
            graph[n] = []
        for i in range(edges):
            a, b = [int(temp) for temp in input().strip().split()]
            graph[a].append(b)
            graph[b].append(a)
        s = int(input())
        ans = solution(graph, s, nodes)
        print(str(ans)[1:-1].replace(",", ""))
