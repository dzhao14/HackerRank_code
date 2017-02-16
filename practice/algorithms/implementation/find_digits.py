#https://www.hackerrank.com/challenges/find-digits

def solution(n):
    arr = [int(d) for d in str(n)]
    count = 0
    for i in arr:
        if i != 0 and n % i == 0:
            count += 1
    return count

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = solution(n)
        print(str(ans))
