#https://www.hackerrank.com/challenges/missing-numbers

def solution(arrN, arrM):
    countN = [0 for i in range(101)]
    countM = [0 for i in range(101)]
    offset = min(arrM)
    for i in arrN:
        countN[i-offset] += 1
    for i in arrM:
        countM[i-offset] += 1

    missing = []
    for i in range(101):
        if countM[i] != countN[i]:
            missing.append(i+offset)
    return missing

if __name__ == '__main__':
    sizen = int(input())
    arrN = [int(temp) for temp in input().strip().split()]
    sizem = int(input())
    arrM = [int(temp) for temp in input().strip().split()]

    ans = solution(arrN, arrM)
    print(str(ans)[1:-1].replace(",",""))
