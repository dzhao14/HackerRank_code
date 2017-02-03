#https://www.hackerrank.com/challenges/hackerland-radio-transmitters

def solution(arr, k):
    count = 0
    lnc = arr[0]
    lastseen = arr[0]
    lastTower = arr[0] - k - 1

    for i in arr:
        #update lnc somehow
        if lnc != -1 and i - lnc == k:
            lastTower = i
            count += 1
            lnc = -1
        if lnc != -1 and i - lnc > k:
            lastTower = lastseen
            count += 1
            lnc = -1
        #i=-1 or i-lnc < k
        if i - lastTower <= k:
            lastseen = i
        elif i - lastTower > k and lnc == -1:
            lnc = i
            lastseen = i
        elif i - lastTower > k and lnc != -1:
            lastseen = i
    if lnc != -1:
        count += 1
        
            

    return count


if __name__ == "__main__":
    size, k = [int(temp) for temp in input().strip().split()]
    arr = [int(temp) for temp in input().strip().split()]
    ans = solution(sorted(arr), k)
    print(str(ans))
