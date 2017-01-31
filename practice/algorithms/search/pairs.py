#https://www.hackerrank.com/challenges/pairs

def pairs(n, k):
    count = 0
    complements = {}
    for i in n:
        pospair = i + k
        negpair = i - k
        if pospair in complements:
            count += complements[pospair]
            
        if negpair in complements:
            count += complements[negpair]
            
        if i in complements:
            complements[i] += 1
        else:
            complements[i] = 1

    return count
        

if __name__ == '__main__':
    n, k = [int(temp) for temp in input().strip().split()]
    arr = [int(temp) for temp in input().strip().split()]
    ans = pairs(arr, k)
    print(str(ans))
    
