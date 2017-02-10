#https://www.hackerrank.com/challenges/bon-appetit

def solution(arr, k, charge):
    shared = sum(arr)-arr[k]
    real = int(shared / 2)
    if real == charge:
        return "Bon Appetit"
    else:
        return abs(charge - real)
    

if __name__ == "__main__":
    size, k = [int(t) for t in input().strip().split()]
    arr = [int(t) for t in input().strip().split()]
    charge = int(input())
    ans = solution(arr, k, charge)
    print(str(ans))
