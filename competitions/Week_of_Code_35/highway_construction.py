#https://www.hackerrank.com/contests/w35/challenges/highway-construction

def f(a,b,m):
    """
    return a^b % m
    """
    X = a
    E = b
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n, k = [int(_) for _ in input().strip().split()]
        sum_ = 0
        for i in range(2, n):
            sum_ = pow(i,k,1000000009)
    print (sum_)
