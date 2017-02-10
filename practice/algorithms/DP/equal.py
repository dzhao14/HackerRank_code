#https://www.hackerrank.com/challenges/equal
#not solved

def moves(i, m):
    diff = i - m
    count = 0
    while diff > 0:
        if diff >= 5:
            count += 1
            diff -= 5
        elif diff >= 2:
            count += 1
            diff -= 2
        else:
            count += 1
            diff -= 1
    return count

def solution(arr):
    count = 0
    m = min(arr)
    for i in arr:
        if i == m:
            pass
        else:
            count += moves(i, m)
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = [int(temp) for temp in input().strip().split()]
        ans = solution(arr)
        print(str(ans))
