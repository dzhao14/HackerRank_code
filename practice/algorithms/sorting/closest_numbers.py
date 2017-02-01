#https://www.hackerrank.com/challenges/closest-numbers

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
        #print(str(arr)[1:-1].replace(",", ""))
        qsort_inplace(arr, lo, indexL)
        qsort_inplace(arr, indexL + 1, hi)

def minPairs(arr):
    m = arr[1] - arr[0]
    pairs = [[arr[0], arr[1]]]

    for i in range(1, len(arr) - 1):
        if arr[i+1] - arr[i] < m:
            m = arr[i+1] - arr[i]
            pairs = [[arr[i], arr[i+1]]]
        elif arr[i+1] - arr[i] == m:
            pairs.append([arr[i], arr[i+1]])
        else:
            pass
    return pairs

if __name__ == '__main__':
    size = int(input().strip())
    arr = [int(temp) for temp in input().strip().split()]

    qsort_inplace(arr, 0, size)
    ans = minPairs(arr)
    print(str(ans).replace("[","").replace("]","").replace(",",""))
    
