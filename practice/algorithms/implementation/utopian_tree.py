#https://www.hackerrank.com/challenges/utopian-tree

def solution(n, h, spring):
    if n == 0:
        return h
    elif spring:
        return solution(n - 1, 2*h, False)
    else:
        return solution(n - 1, h + 1, True)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = solution(n, 1, True)
        print(str(ans))
