#https://www.hackerrank.com/challenges/gem-stones

def solution(arr):
    count = 0
    for i in range(97, 123):
        if all([chr(i) in n for n in arr]):
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        s = input().strip()
        arr.append(s)
    ans = solution(arr)
    print(str(ans))
