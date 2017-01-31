#https://www.hackerrank.com/challenges/find-the-median

#only for nonnegative numbers
def median_counting(arr, rank, upper):
    counts = [0 for i in range(upper)]
    sums = [0 for i in range(upper)]
    for i in range(len(arr)):
        counts[arr[i]] += 1
    tot = 0
    for i in range(upper):
        tot += counts[i]
        sums[i] = tot
    output = [0 for i in range(len(arr))]
    for i in arr:
        if sums[i] -1 == rank:
            return i
        else:
            output[sums[i] - 1] = i
            sums[i] -= 1

#stable
def median(arr, offset, rank):
    if len(arr) <= 1:
        return arr[0]
    
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    pivotLoc = offset + len(left)
    newoffset = offset + 1 + len(left)
    if pivotLoc > rank:
        return median(left, offset, rank)
    elif pivotLoc < rank:
        return median(right, newoffset, rank)
    else:
        return pivot

#unstable
def median_inplace(arr, lo, hi, rank):
    if hi - lo <= 1:
        return arr[lo]
    else:
        pivot = arr[hi-1]
        indexL = lo
        for i in range(lo, hi):
            if arr[i] <= pivot:
                temp = arr[indexL]
                arr[indexL] = arr[i]
                arr[i] = temp
                indexL += 1
        indexL -= 1

        if indexL > rank:
            return median(arr, lo, indexL, rank)
        elif indexL < rank:
            return median(arr, indexL + 1, hi, rank)
        else:
            return arr[indexL]

if __name__ == '__main__':
    pass
##    size = int(input())
##    arr = [int(temp) for temp in input().strip().split()]
##    ans = median(arr, 0, len(arr)//2)
##    print(str(ans))
    
