#https://www.hackerrank.com/contests/101hack46/challenges/marcs-cakewalk

def solution(size, arr):
    sarr = sorted(arr)
    miles = 0
    c = 0
    for i in range(len(sarr)-1,-1,-1):
        miles += pow(2,c) * sarr[i]
        c += 1
    return miles

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(size, arr)
    print(str(ans))
