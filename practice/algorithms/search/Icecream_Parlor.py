#https://www.hackerrank.com/challenges/icecream-parlor

def solution(arr, cash):
    dic = {}
    for i in range(len(arr)):
        if cash-arr[i] in dic:
            return (dic[cash-arr[i]], i+1)
        else:
            dic[arr[i]] = i+1

if __name__ == "__main__":
    trips = int(input())
    for t in range(trips):
        cash = int(input())
        flavs = int(input())
        arr = [int(temp) for temp in input().strip().split()]
        ans = solution(arr, cash)
        print(str(ans[0]) + " " + str(ans[1]))
            
