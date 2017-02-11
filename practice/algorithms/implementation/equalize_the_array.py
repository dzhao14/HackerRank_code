#https://www.hackerrank.com/challenges/equality-in-a-array

def solution(arr):
    counter = [0 for i in range(101)]
    for i in arr:
        counter[i] += 1
    s = sum(counter)
    m = max(counter)
    return s-m

if __name__ == "__main__":
    n = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
