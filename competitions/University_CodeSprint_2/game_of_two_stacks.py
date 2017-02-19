#https://www.hackerrank.com/contests/university-codesprint-2/challenges/game-of-two-stacks

def bSearch(arr, lo, hi, target):
    if len(arr) == 0:
        return -1
    if lo == hi:
        return lo
    mid = lo + (hi-lo)//2
    item = arr[mid]
    if target <= item:
        return bSearch(arr, lo, mid, target)
    else:
        return bSearch(arr, mid+1, hi, target)
    
#This gross function is worth 15 points
def solution(arrn, arrm, x):
    save = [0 for i in range(x+1)]
    count = 0
    sc = arrn[0]
    idx = 1
    i = 0
    arrn.append(99999999999)
    while i <= x:
        if idx >= len(arrn):
            save[i] = count
        elif i < sc:
            save[i] = count
        else:
            count += 1
            save[i] = count
            sc += arrn[idx]
            idx += 1
        if arrn[idx-1] != 0:
            i += 1
    if sc == x:
        while arrn[idx] == 0 and idx < len(arrn):
            save[x] += 1
            idx += 1
    print(save)
    count = 0
    maxcount = save[x]
    tot = 0
    for i in arrm:
        count += 1
        tot += i
        now = x - tot
        if now < 0:
            break
        maxcount = max(maxcount, count + save[now])
    return maxcount

# I think this is too slow. But it works and I only timed-out on the
# biggest test case.
def solution2(arrn, arrm, x):
    
    sn = []
    for i in range(len(arrn)):
        if i == 0:
            sn.append(arrn[i])
        else:
            sn.append(arrn[i] + sn[i-1])
    sm = []
    for i in range(len(arrm)):
        if i == 0:
            sm.append(arrm[i])
        else:
            sm.append(arrm[i] + sm[i-1])
    #print(sn)
    #print(sm)
    maxcount = 0
    idxn = bSearch(sn, 0, len(sn)-1, x+1)
    if idxn == len(sn)-1 and sn[idxn] <= x:
        maxcount = idxn+1
    else:
        maxcount = idxn
    #print("maxcount: " + str(maxcount))
    for i in range(len(sm)):
        target = x - sm[i]

        if target < 0:
            break

        idx = bSearch(sn, 0, len(sn)-1, target+1)
        if idx == len(sn)-1 and sn[idx] <= target:
            maxcount = max(maxcount, idx+1+i+1)
            
        else:
            maxcount = max(maxcount, idx+i+1)

    return maxcount
        

if __name__ == "__main__":
    g = int(input())
    for i in range(g):
        n, m, x = [int(t) for t in input().strip().split()]
        arrn = [int(t) for t in input().strip().split()]
        arrm = [int(t) for t in input().strip().split()]
        ans = solution2(arrn, arrm, x)
        print(str(ans))        
