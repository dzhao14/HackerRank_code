#https://www.hackerrank.com/contests/world-codesprint-12/challenges/red-knights-shortest-path

import queue


if __name__ == "__main__":
    n = int(input())
    i, j, u, v = [int(_) for _ in input().split()]
    seen = [[0 for _ in range(n)] for j in range(n)]
    seen[i][j] = 1
    parent = [[(-1, -1) for _ in range(n)] for j in range(n)]
    moves = [["" for _ in range(n)] for j in range(n)]
    visit = queue.Queue()
    visit.put((i, j))
    while visit.qsize() > 0:
        at = visit.get()
        a, b = at
        if (a == u and b == v):
            break
        if a-2 >= 0 and b-1 >= 0 and seen[a-2][b-1] == 0:
            seen[a-2][b-1] = 1
            parent[a-2][b-1] = at
            visit.put((a-2, b-1))
            moves[a-2][b-1] = "UL"
        if a-2 >= 0 and b+1 < n and seen[a-2][b+1] == 0:
            seen[a-2][b+1] = 1
            parent[a-2][b+1] = at
            visit.put((a-2, b+1))
            moves[a-2][b+1] = "UR"
        if b+2 < n and seen[a][b+2] == 0:
            seen[a][b+2] = 1
            parent[a][b+2] = at
            visit.put((a,b+2))
            moves[a][b+2] = "R"
        if a+2 < n and b+1 < n and seen[a+2][b+1] == 0:
            seen[a+2][b+1] = 1
            parent[a+2][b+1] = at
            visit.put((a+2, b+1))
            moves[a+2][b+1] = "LR"
        if a+2 < n and b-1 >= 0 and seen[a+2][b-1] == 0:
            seen[a+2][b-1] = 1
            parent[a+2][b-1] = at
            visit.put((a+2, b-1))
            moves[a+2][b-1] = "LL"
        if b-2 >= 0 and seen[a][b-2] == 0:
            seen[a][b-2] = 1
            parent[a][b-2] = at
            visit.put((a, b-2))
            moves[a][b-2] = "L"

    if seen[u][v] != 1:
        print("Impossible")
    else:
        sol = []
        s = u
        f = v
        while parent[s][f] != (-1, -1):
            sol.append(moves[s][f])
            temp = parent[s][f][0]
            temp2 = parent[s][f][1]
            s = temp
            f = temp2
        print(len(sol))
        print(str(sol[::-1])[1:-1].replace(",", "").replace('\'', ""))
