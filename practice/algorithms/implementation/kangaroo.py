#https://www.hackerrank.com/challenges/kangaroo

def solution(x1, v1, x2, v2):
    deltax = v1 - v2
    deltas = x2 - x1
    if deltax == 0 and x1 != x2:
        return "NO"
    if deltax == 0 and x1 == x2:
        return "YES"
    if deltas / deltax < 0:
        return "NO"
    if deltas % deltax != 0:
        return "NO"
    return "YES"

if __name__ == "__main__":
    x1, v1, x2, v2 = [int(temp) for temp in input().strip().split()]
    ans = solution(x1, v1, x2, v2)
    print(ans)
