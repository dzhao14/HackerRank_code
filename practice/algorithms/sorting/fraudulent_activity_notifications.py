#https://www.hackerrank.com/challenges/fraudulent-activity-notifications

def median_counting(arr, lo, hi, ranks):
    counts = [0 for i in range(201)]
    sums = [0 for i in range(201)]
    for i in range(lo, hi):
        counts[arr[i]] += 1
    tot = 0
    for i in range(201):
        tot += counts[i]
        sums[i] = tot
    output = [0 for i in range(len(arr))]
  
    for i in range(lo, hi):
        output[sums[arr[i]] - 1] = arr[i]
        sums[arr[i]] -= 1

    if len(ranks) == 1:
        return output[ranks[0]]
    else:
        return (output[ranks[0]] + output[ranks[1]]) / 2

def reports(arr, d):
    count = 0
    if d % 2 == 0:
        med = median_counting(arr, 0, d, [d//2, d//2 - 1])
        for i in range(d, len(arr)):
            if arr[i] >= 2 * med:
                count += 1
            med = median_counting(arr, i-d+1, i+1, [d//2, d//2 - 1])
        return count
    else:
        med = median_counting(arr, 0, d, [d//2])
        for i in range(d, len(arr)):
            if arr[i] >= 2 * med:
                count += 1
            med = median_counting(arr, i-d + 1, i+1, [d//2])
        return count
        

if __name__ == '__main__':
    size, d = [int(temp) for temp in input().strip().split()]
    arr = [int(temp) for temp in input().strip().split()]

    ans = reports(arr, d)
    print(str(ans))
