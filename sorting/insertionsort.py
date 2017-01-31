def insertionSort(arr):
    if len(arr) <= 0:
        return arr
    return insert(arr[0], insertionSort(arr[1:]))
    
def insert(v, arr):
    sol = []
    if len(arr) == 0:
        return [v]
    for i in range(len(arr)):
        if v >= arr[i]:
            sol.append(arr[i])
        elif v < arr[i]:
            sol.append(v)
            sol = sol + arr[i:]
            return sol
    sol.append(v)
    return sol

if __name__ == '__main__':
    size = int(input())
    arr = [int(temp) for temp in input().strip().split()]
    ans = insertionSort(arr)
    print(str(ans)[1:-1].replace(',', ""))
