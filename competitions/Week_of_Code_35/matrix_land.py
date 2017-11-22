#https://www.hackerrank.com/contests/w35/challenges/matrix-land

# O(1)
def calcMoveCost(sums, i, j):
    if i > j:
        temp = i
        i = j
        j = temp
    if i == 0:
        return sums[j]
    else:
        return sums[j] - sums[i-1]

# O(M)
def calcSums(table, row):
    sums = [0 for i in range(len(table[row]))]
    for i in range(len(table[row])):
        if i == 0:
            sums[i] = table[row][i]
        else:
            sums[i] = table[row][i] + sums[i-1]
    return sums

# O(M)
def calcRow(table, row, n, m):
    max_left = [0 for i in range(m)]
    max_right = [0 for i in range(m)]
    for i in range(m-1, -1, -1):
        if i == m-1:
            max_left[i] = table[row][i]
        else:
            max_left[i] = max(table[row][i], max_left[i+1] + table[row][i])
    for i in range(m):
        if i == 0:
            max_right[i] = table[row][i]
        else:
            max_right[i] = max(table[row][i], max_right[i-1] + table[row][i])
    return max_left, max_right

# O(M)
def calcBest(table, row, n, m):
    best = [0 for i in range(m)]
    max_left = [0 for i in range(m)]
    max_right = [0 for i in range(m)]
    for i in range(m-1, -1, -1):
        if i == m-1:
            max_left[i] = table[row][i]
        else:
            max_left[i] = max(table[row][i], max_left[i+1] + table[row][i])
    for i in range(m):
        if i == 0:
            max_right[i] = table[row][i]
        else:
            max_right[i] = max(table[row][i], max_right[i-1] + table[row][i])
    for i in range(m):
        best[i] = max(max_right[i], max_left[i],
                   max_right[i] + max_left[i] - table[row][i])
    return best

# O(N*M^2)
def solution(table, n, m):
    best = calcBest(table, 0, n, m)
    next_best = [0 for i in range(m)]
    temp = [0 for i in range(m)]
    for i in range(1, n):
        max_left, max_right = calcRow(table, i, n, m)
        next_best = [0 for i in range(m)]
        sums = calcSums(table, i)
        for endidx in range(m):
            for startidx in range(m):
                temp[startidx] = (best[startidx] +
                                  calcMoveCost(sums, startidx, endidx))
                if min(startidx, endidx) != 0:
                    temp[startidx] = max(temp[startidx],
                        temp[startidx] + max_right[min(startidx,endidx)-1])
                if max(startidx, endidx) != m-1:
                    temp[startidx] = max(temp[startidx],
                        temp[startidx] + max_left[max(startidx, endidx)+1])
            next_best[endidx] = max(temp)
        
        best = next_best
        
    return max(best)
    

if __name__ == "__main__":
    n, m = [int(_) for _ in input().strip().split()]
    table = []
    for i in range(n):
        table.append([int(_) for _ in input().strip().split()])

    ans = solution(table, n, m)
    print(ans)
