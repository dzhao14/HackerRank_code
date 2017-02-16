#https://www.hackerrank.com/challenges/cut-the-sticks

def solution(arr):
    sarr = sorted(arr, reverse = True)
    while len(sarr) > 0:
        print(len(sarr))
        c = sarr[-1]
        for i in range(len(sarr)):
            sarr[i] -= c
        cut = 0
        for i in range(len(sarr)-1,-1,-1):
            if sarr[i] != 0:
                break
            cut -= 1
        sarr = sarr[:cut]

if __name__ == "__main__":
    n = int(input())
    arr = [int(t) for t in input().strip().split()]
    solution(arr)
