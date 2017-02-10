#https://www.hackerrank.com/challenges/between-two-sets

def areFactorsOf(nr, a):
    for i in nr:
        if a % i != 0:
            return False
    return True

def isFactorOf(mr, a):
    for i in mr:
        if i % a != 0:
            return False
    return True

def solution(nr, mr):
    count = 0
    low = max(nr)
    high = min(mr)
    for i in range(low, high+1):
        if areFactorsOf(nr, i):
            if isFactorOf(mr, i):
                count += 1
        else:
            pass
    return count

if __name__ =="__main__":
    n, m = [int(temp) for temp in input().strip().split()]
    nr = [int(temp) for temp in input().strip().split()]
    mr = [int(temp) for temp in input().strip().split()]
    ans = solution(nr, mr)
    print(str(ans))
