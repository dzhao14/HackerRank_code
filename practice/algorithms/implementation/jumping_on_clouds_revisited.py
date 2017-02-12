#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

def solution(arr, k, n):
    done = False
    idx = 0
    e = 100
    while not done:
        idx = (idx + k) % n
        if arr[idx] == 0:
            e -= 1
        else:
            e -= 3
        if idx == 0:
            done = True
    return e

if __name__ == "__main__":
    n, k = [int(t) for t in input().strip().split()]
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr, k, n)
    print(str(ans))
