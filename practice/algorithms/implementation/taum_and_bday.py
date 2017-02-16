#https://www.hackerrank.com/challenges/taum-and-bday

def solution(b, w, x, y, z):
    if (x + z) > y and (y + z) > x:
        return b * x + w * y
    if (x + z) < y:
        return (b+w) * x + w * z
    else:
        return (b+w) * y + b * z

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
       b, w = [int(t) for t in input().strip().split()]
       x, y, z = [int(t) for t in input().strip().split()]
       ans = solution(b, w, x, y, z)
       print(str(ans))
