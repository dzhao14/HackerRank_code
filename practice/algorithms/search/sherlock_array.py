#https://www.hackerrank.com/challenges/sherlock-and-array

def solution(arr):
    leftS = 0
    rightS = 0
    totS = sum(arr)
    rightS = totS - arr[0]
    if leftS == rightS:
        return "YES"
    for i in range(len(arr)-1):
        if leftS == rightS:
            return "YES"
        else:
            leftS += arr[i]
            rightS -= arr[i+1]
    return "NO"

if __name__ == "__main__":
    tests = int(input())
    for t in range(tests):
        size = int(input())
        arr = [int(temp) for temp in input().strip().split()]
        ans = solution(arr)
        print(ans)
