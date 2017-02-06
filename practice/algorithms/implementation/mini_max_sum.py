#https://www.hackerrank.com/challenges/mini-max-sum

def solution(arr):
    Sarr = sorted(arr)
    a1 = sum(Sarr[:4])
    a2 = sum(Sarr[1:])
    return (a1,a2)

if __name__ == "__main__":
    arr = [int(temp) for temp in input().strip().split()]
    ans = solution(arr)
    print(str(ans)[1:-1].replace(",",""))
