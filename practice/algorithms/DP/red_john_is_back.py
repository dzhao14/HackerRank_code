#https://www.hackerrank.com/challenges/red-john-is-back


#http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

#Not totally sure how Sieve of Eratosthenes works but I understand the DP part
def solution(n, idx, bricks, memo):
    key = (idx, bricks)
    if key in memo:
        return memo[key]
    if idx > n+1 and n!=n+4:
        return 0
    if idx == n+1 or idx == n+4:
        return 1
    else:
        memo[key] = (solution(n, idx + 1, bricks + 1, memo) +
                     solution(n, idx + 4, bricks + 1, memo))
        return memo[key]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        memo = {}
        ways = solution(n, 1, 0, memo)
        print(str(len(get_primes_erat(ways+1))))
