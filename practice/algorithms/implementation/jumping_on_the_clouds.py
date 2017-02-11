#https://www.hackerrank.com/challenges/jumping-on-the-clouds

def solution(arr):
    jumps = 0
    loc = 0
    while loc != len(arr)-1:
        if loc == len(arr)-2:
            jumps += 1
            loc += 1
        elif arr[loc+2] != 1:
            jumps += 1
            loc += 2
        else:
            jumps += 1
            loc += 1
    return jumps

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
