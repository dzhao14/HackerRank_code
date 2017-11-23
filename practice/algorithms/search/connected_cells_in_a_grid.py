#https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

def getSize(table, i, j, n, m, seen):
    seen[i][j] = 1
    size = 1
    if j > 0 and i > 0 and table[i-1][j-1] == 1 and seen[i-1][j-1] != 1:
        size += getSize(table, i-1, j-1, n, m, seen)
    if i > 0 and table[i-1][j] == 1 and seen[i-1][j] != 1:
        size += getSize(table, i-1, j, n, m, seen)
    if j < m-1 and i > 0 and table[i-1][j+1]==1 and seen[i-1][j+1]!=1:
        size += getSize(table, i-1, j+1, n, m, seen)
    if j>0 and table[i][j-1]==1 and seen[i][j-1] !=1:
        size += getSize(table, i, j-1, n, m, seen)
    if j < m-1 and table[i][j+1]==1 and seen[i][j+1]!=1:
        size += getSize(table, i, j+1, n, m, seen)
    if i < n-1 and j>0 and table[i+1][j-1]==1 and seen[i+1][j-1] != 1:
        size += getSize(table, i+1, j-1, n, m, seen)
    if i < n-1 and table[i+1][j]==1 and seen[i+1][j] != 1:
        size += getSize(table, i+1, j, n, m, seen)
    if i < n-1 and j < m-1 and table[i+1][j+1]==1 and seen[i+1][j+1]!=1:
        size += getSize(table, i+1, j+1, n, m, seen)
    return size

def solution(table, n, m):
    seen = [[0 for i in range(m)] for j in range(n)]
    max_ = 0
    for i in range(n):
        for j in range(m):
            if seen[i][j] == 0 and table[i][j] == 1:
                size = getSize(table, i, j, n, m, seen)
                max_ = max(max_, size)
    return max_

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    table = []
    for i in range(n):
        table.append([int(_) for _ in input().strip().split()])
    ans = solution(table, n, m)
    print(ans)
