#https://www.hackerrank.com/contests/rookierank-2/challenges/prefix-neighbors
#not solved

def value(s):
    count = 0
    for i in s:
        count += ord(i)
    return count

#too slow and probably wrong
def bruteforce(arr):
    pneib1 = {}
    pneib2 = {}
    sarr = sorted(arr)
    for i in range(len(sarr)):
        s1 = sarr[i]
        for j in range(i + 1, len(sarr)):
            s2 = sarr[j]
            if len(s2) <= len(s1):
                break
            if s1 == s2[:len(s1)]:
                if (s1, i) in pneib1:
                    if len(s2) < len(pneib1[(s1, i)]):
                        pneib1[(s1, i)] = s2
                        pneib2[(s2, j)] = s1
                else:
                    pneib1[(s1, i)] = s2
                    pneib2[(s2, j)] = s1
            else:
                break
    cant = []
    count = 0
    for i in range(len(sarr)-1,-1,-1):
        s = sarr[i]
        if s in cant:
            continue
        if (s, i) in pneib2:
            count += value(s)
            cant.append(pneib2[(s, i)])
        else:
            count += value(s)
    return count

#wrong
import bisect
def secondattempt(arr):
    sarr = sorted(arr)
    has = {}
    for i in range(1, 12):
        has[i] = []
    count = 0
    for i in range(len(sarr)-1,-1,-1):
        s1 = sarr[i]
        l = len(s1)
        neib = False
        for i in range(l+1,12):
            b = False
            for s2 in has[i]:
                if s2[:l] > s1:
                    break
                if s1 == s2[:l]:
                    has[i].remove(s2)
                    neib = True
                    b = True
                    break
            if b:
                break
        if not neib:
            count += value(s1)
            bisect.insort(has[l], s1)
    return count
                

if __name__ == "__main__":
    size = int(input())
    arr = [t for t in input().split()]
    ans = secondattempt(arr)
    print(str(ans))
