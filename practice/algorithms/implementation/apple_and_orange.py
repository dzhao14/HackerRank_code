#https://www.hackerrank.com/challenges/apple-and-orange

def solution(a, b, s, t, arrA, arrB):
    apple = 0
    orange = 0
    for i in arrA:
        if a + i >= s and a + i <= t:
            apple += 1
    for i in arrB:
        if b + i >= s and b + i <= t:
            orange += 1
    return (apple, orange)

if __name__ == "__main__":
    s, t = [int(t) for t in input().strip().split()]
    a, b = [int(t) for t in input().strip().split()]
    m, n = [int(t) for t in input().strip().split()]
    arrA = [int(t) for t in input().strip().split()]
    arrB = [int(t) for t in input().strip().split()]
    ans = solution(a, b, s, t, arrA, arrB)
    for i in ans:
        print(str(i))
