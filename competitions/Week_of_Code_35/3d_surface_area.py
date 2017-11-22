#https://www.hackerrank.com/contests/w35/challenges/3d-surface-area

def solution(table, h, w):
    area = h * w * 2
    for i in range(h):
        for j in range(w):
            height = table[i][j]
            if i == 0:
                area += height
            if j == 0:
                area += height
            if i == h-1:
                area += height
            if j == w-1:
                area += height
            if i != 0:
                area += max(height - table[i-1][j],0)
            if j != 0:
                area += max(height - table[i][j-1],0)
            if i != h-1:
                area += max(height - table[i+1][j],0)
            if j != w-1:
                area += max(height - table[i][j+1],0)
    return area
    

if __name__ == "__main__":
    h, w = [int(_) for _ in input().strip().split()]
    table = []
    for i in range(h):
        row = [int(_) for _ in input().strip().split()]
        table.append(row)
    ans = solution(table, h, w)
    print(ans)
