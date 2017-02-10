#https://www.hackerrank.com/challenges/divisible-sum-pairs

def solution(arr, k):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) % k == 0:
                count += 1
    return count

if __name__ == "__main__":
    n, k = [int(t) for t in input().strip().split()]
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr, k)
    print(str(ans))
