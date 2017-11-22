#https://www.hackerrank.com/contests/w35/challenges/triple-recursion

def solution(n, m, k):
    mat = [[0 for y in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                mat[i][j] = m
            elif i == j:
                mat[i][j] = mat[i-1][j-1] + k
            elif i > j:
                mat[i][j] = mat[i-1][j] - 1
            else:
                mat[i][j] = mat[i][j-1] - 1

    return mat
            

if __name__ == "__main__":
    n, m, k = [int(_) for _ in input().strip().split()]
    mat = solution(n, m, k)
    for row in mat:
        print(str(row).replace(",", "")[1:-1])
