#https://www.hackerrank.com/challenges/sock-merchant

def solution(arr):
    counter = [0 for i in range(101)]
    for i in arr:
        counter[i] += 1
    count = 0
    for i in counter:
        count += i//2
    return count

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans))

