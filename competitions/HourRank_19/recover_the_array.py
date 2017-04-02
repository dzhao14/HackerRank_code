#https://www.hackerrank.com/contests/hourrank-19/challenges/recover-the-array

def solution(arr):
    count = 0
    number = arr[0]
    idx = 1
    while idx < len(arr):
        idx += number
        count += 1
        if idx < len(arr):
            number = arr[idx]
            idx += 1
        else:
            break

    return count
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = [int(_) for _ in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
