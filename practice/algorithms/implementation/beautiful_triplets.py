#https://www.hackerrank.com/challenges/beautiful-triplets

def solution(arr, d):
    count = 0
    for j in range(len(arr)):
        low = False
        high = False
        for i in range(j):
            if arr[j] - arr[i] == d:
                low = True
                break
            if arr[j] - arr[i] < d:
                break
        for k in range(j, len(arr)):
            if arr[k] - arr[j] == d:
                high = True
                break
            if arr[k] - arr[j] > d:
                break
        if low and high:
            count += 1
    return count
        

if __name__ == "__main__":
    n, d = [int(t) for t in input().strip().split()]
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr, d)
    print(str(ans))
