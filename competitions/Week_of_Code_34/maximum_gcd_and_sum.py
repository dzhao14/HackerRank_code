#https://www.hackerrank.com/contests/w34/challenges/maximum-gcd-and-sum

import math

#finished_factors = {}

def factors(n):
##    if n in finished_factors:
##        return finished_factors[n]
    
    out = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            out.append(i)
            out.append(n//i)
##    finished_factors[n] = out
    return out
        
    
def solution(n, a, b):
    #Is this number in a?
    possible_a = [0 for _ in range(1000001)]

    #Is this number in b?
    possible_b = [0 for _ in range(1000001)]

    #The largest number in a that has this factor
    factor_a = [0 for _ in range(1000001)]
    
    for i in a:
        if possible_a[i] == 0:
            for factor in factors(i):
                if i > factor_a[factor]:
                    factor_a[factor] = i
            possible_a[i] = 1
        else:
            continue
    max_shared_fac = 1
    max_sum = -1
    for i in b:
        if possible_b[i] == 0:
            for factor in factors(i):
                if factor == max_shared_fac and factor_a[factor] != 0:
                    if i + factor_a[factor] > max_sum:
                        max_sum = i + factor_a[factor]
                elif factor > max_shared_fac and factor_a[factor] != 0:
                    max_sum = i + factor_a[factor]
                    max_shared_fac = factor
                else:
                    continue
            possible_b[i] = 1
        else:
            continue

    return max_sum
    

if __name__ == "__main__":
    n = int(input())
    a = [int(_) for _ in input().strip().split()]
    b = [int(_) for _ in input().strip().split()]
    ans = solution(n, a, b)
    print(str(ans))
