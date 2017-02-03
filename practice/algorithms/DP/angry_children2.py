#https://www.hackerrank.com/challenges/angry-children-2
#not solved

best = {}
best["best"] = 10000000000

def done(arr):
   return arr[1:] == arr[:-1]

def updateLow(curlow, num):
    if num < curlow or curlow == -1:
        return num
    else:
        return curlow

def updateHi(curhi, num):
    if num > curhi or curhi == -1:
        return num
    else:
        return curhi

def minK(arr, lo, hi, amt, idx, k, memo):
    key = (lo, hi, amt, idx)
    if key in memo:
        memo[key] = True
        return
    if hi - lo >= best["best"]:
        memo[key] = True
        return
    if amt == k:
        memo[key] = True
        best["best"] = hi - lo
        return
    if amt > k:
        memo[key] = True
        return
    if idx >= len(arr):
        memo[key] = True
        return
    else:
        num = arr[idx]
        minK(arr, lo, hi, amt, idx+1, k, memo)
        minK(arr, updateLow(lo, num), updateHi(hi, num), amt+1, idx+1, k, memo)
        
    

if __name__ == '__main__':
    size = int(input())
    k = int(input())
    arr = []
    for i in range(size):
        num = int(input())
        arr.append(num)

    memo = {}
    minK(arr, -1, -1, 0, 0, k, memo)
    ans = best["best"] + ((best["best"] / 2) * (k - 2)) * 2
    print(str(ans))
        
