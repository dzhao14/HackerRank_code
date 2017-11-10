#Binary search!

#lo and hi are inclusive
def bSearchRecursive(arr, lo, hi, target):
    """
    Recursive
    """
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

#lo and hi are inclusive
def bSearchIterative(arr, lo, hi, target):
    """
    Iterative
    """
    if len(arr) == 0:
        return -1
    
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if target > arr[mid]:
            lo = mid + 1
        else: 
            hi = mid

    return lo if arr[lo] == target else -1
