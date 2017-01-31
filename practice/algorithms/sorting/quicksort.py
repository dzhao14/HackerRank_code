#https://www.hackerrank.com/challenges/quicksort2

#returns new sorted array
def qsort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    left = qsort(left)
    right = qsort(right)
    return left + [pivot] + right

#https://www.hackerrank.com/challenges/quicksort3

#mutates given array
#lo is the index of the first guy in this sub-array
#hi is the index of the last guy in the sub-array + 1
def qsort_inplace(arr, lo, hi):
    if hi - lo <= 1:
        pass
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
        print(str(arr)[1:-1].replace(",", ""))
        qsort_inplace(arr, lo, indexL)
        qsort_inplace(arr, indexL + 1, hi)

if __name__ == '__main__':
    size = int(input())
    arr = [int(temp) for temp in input().strip().split()]
    qsort_inplace(arr, 0, len(arr))
    #print(str(arr)[1:-1].replace(",", ""))

