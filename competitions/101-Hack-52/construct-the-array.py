#https://www.hackerrank.com/contests/101hack52/challenges/construct-the-array

MOD = 1000000007

if __name__ == "__main__":
    n, k, x = [int(_) for _ in input().strip().split()]
    if x == 1:
        p = k-1
    else:
        p = k-2
    total = k-1
    for i in range(2,n-1):
        total = (total * (k-1)) % MOD
        p = (total - p) % MOD
    print(p)
