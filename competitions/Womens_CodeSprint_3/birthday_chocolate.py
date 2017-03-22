#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/the-birthday-bar

def works(arr, d, m, start):
    if sum(arr[start:start+m]) == d:
        return True
    else:
        return False

def solution(arr, d, m):
    count = 0
    for i in range(len(arr) - (m - 1)):
        if works(arr, d, m, i):
            count += 1
    return count

if __name__ == "__main__":
    size = input().strip()
    arr = [int(_) for _ in input().strip().split()]
    d, m = [int(_) for _ in input().strip().split()]
    ans = solution(arr, d, m)
    print(str(ans))
