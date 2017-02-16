#https://www.hackerrank.com/challenges/service-lane

def solution(i, j, anr):
    return min(anr[i:j+1])

if __name__ == "__main__":
    n, t = [int(_) for _ in input().strip().split()]
    arr = [int(_) for _ in input().strip().split()]
    for i in range(t):
        i, j = [int(_) for _ in input().strip().split()]
        ans = solution(i, j, arr)
        print(str(ans))
    
