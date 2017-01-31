import math

def mergeSort(n, lo, hi):
    if hi - lo == 1:
        return [n[lo]]
    mid = math.floor(lo + (hi - lo)/2)
    leftH = mergeSort(n, lo, mid)
    rightH = mergeSort(n, mid, hi)

    join = []
    l = 0
    r = 0

    while l < len(leftH) and r < len(rightH):
        if leftH[l] < rightH[r]:
            join.append(leftH[l])
            l += 1

        else:
            join.append(rightH[r])
            r += 1

    while l < len(leftH):
        join.append(leftH[l])
        l += 1

    while r < len(rightH):
        join.append(rightH[r])
        r += 1

    return join
