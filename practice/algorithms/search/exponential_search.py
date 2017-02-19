#Binary search!

#lo and hi are inclusive
def bSearch(arr, lo, hi, target):
    if len(arr) == 0:
        return -1
    if lo == hi:
        return lo if arr[lo] == target else -1
    mid = lo + (hi-lo)//2
    item = arr[mid]
    if target <= item:
        return bSearch(arr, lo, mid, target)
    else:
        return bSearch(arr, mid+1, hi, target)

#http://www.geeksforgeeks.org/exponential-search/
def expSearch(arr, target):
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] <= target:
        i = i*2

    return bSearch(arr, i//2, min(i, len(arr)-1), target)
