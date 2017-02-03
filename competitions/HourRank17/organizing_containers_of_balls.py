#https://www.hackerrank.com/contests/hourrank-17/challenges/organizing-containers-of-balls
#not solved

def solution(matrix, size):
    for i in range(size):
        rowSum = 0
        colSum = 0
        for r in matrix[i]:
            rowSum += r
        for c in range(size):
            colSum += matrix[c][i]
        if colSum != rowSum:
            return False
    return True
        

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        print(i)
        matrix = []
        size = int(input())
        for r in range(size):
            row = [int(temp) for temp in input().strip().split()]
            matrix.append(row)
        ans = solution(matrix, size)
        if ans:
            print("Possible")
        else:
            print("Impossible")
