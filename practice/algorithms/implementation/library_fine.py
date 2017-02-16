#https://www.hackerrank.com/challenges/library-fine

def solution(d, m, y, rd, rm, ry):
    if ry - y > 0:
        return 10000
    elif ry - y < 0:
        return 0
    if rm - m > 0:
        return (rm - m) * 500
    elif ry - y == 0 and rm - m < 0:
        return 0
    if rd - d > 0:
        return (rd - d) * 15
    elif rm - m == 0 and rd - d < 0:
        return 0
    else:
        return 0

if __name__ == "__main__":
    rd, rm, ry = [int(t) for t in input().strip().split()]
    d, m, y = [int(t) for t in input().strip().split()]
    ans = solution(d, m, y, rd, rm, ry)
    print(str(ans))
