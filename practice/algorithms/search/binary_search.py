#Binary search!

#lo and hi are inclusive
def bSearch(arr, lo, hi, target):
    if lo == hi:
        return lo if arr[lo] == target else -1
    mid = lo + (hi-lo)//2
    item = arr[mid]
    if target <= item:
        return bSearch(arr, lo, mid, target)
    else:
        return bSearch(arr, mid+1, hi, target)
