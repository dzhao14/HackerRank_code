#https://www.hackerrank.com/challenges/coin-change

#This approach works but is too slow
def ways_change(remain, counts, values, coins, memo):
    key = str(remain) + " " + str(counts)
    if key in memo:
        return 0
    if remain < 0:
        memo[key] = 0
        return 0
    if remain == 0:
        memo[key] = 1
        return 1
    else:
        count = 0
        for i in range(coins):
            counts[i] += 1
            count += ways_change(remain-values[i], counts, values, coins, memo)
            counts[i] -= 1
        memo[key] = count
        return count

#Intuition from:
    
#http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

# To count total number solutions, we can divide all set solutions in two sets.
# 1) Solutions that do not contain mth coin (or Sm).
# 2) Solutions that contain at least one Sm.
# Let count(S[], m, n) be the function to count the number of solutions,
#  then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).

def ways_count(rem, vals, notUsed, memo):
    key = (rem, notUsed)
    if key in memo:
        return memo[key]
    if rem < 0:
        return 0
    if rem == 0:
        return 1
    if notUsed == -1:
        return 0
    else:
        memo[key] = (ways_count(rem, vals, notUsed-1, memo)
                     + ways_count(rem - vals[notUsed], vals, notUsed, memo))
        return memo[key]
        
        
if __name__ == '__main__':
    change, coins = [int(temp) for temp in input().strip().split()]
    values = [int(temp) for temp in input().strip().split()]
    memo = {}
    ans = ways_count(change, values, len(values)-1, memo)
    print(str(ans))



