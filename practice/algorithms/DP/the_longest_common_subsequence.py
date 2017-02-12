#https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence

def solution(arr1, arr2, idx1, idx2, memo, ans):
    key = (idx1, idx2)
    if key in memo:
        return memo[key]
    if idx1 < 1 or idx2 < 1:
        return 0
    if arr1[idx1] == arr2[idx2]:
        memo[key] = 1 + solution(arr1, arr2, idx1-1, idx2-1, memo, ans)
        ans[idx1][idx2] = ans[idx1-1][idx2-1] + [arr1[idx1]]
        return memo[key]
    else:
        memo[key] = max(solution(arr1, arr2, idx1-1, idx2, memo, ans),
                           solution(arr1, arr2, idx1, idx2-1, memo, ans))
        l1 = len(ans[idx1][idx2-1])
        l2 = len(ans[idx1-1][idx2])
        if l1 > l2:
            ans[idx1][idx2] = ans[idx1][idx2-1]
        else:
            ans[idx1][idx2] = ans[idx1-1][idx2]
        
        return memo[key]
            
    
if __name__ == "__main__":
    size1, size2 = [int(t) for t in input().strip().split()]
    arr1 = [int(t) for t in input().strip().split()]
    arr1 = [-1] + arr1
    arr2 = [int(t) for t in input().strip().split()]
    arr2 = [-2] + arr2
    ans = []
    for i in range(size1+1):
        ans.append([])
        for j in range(size2+1):
            ans[i].append([])
    length_ans = solution(arr1, arr2, size1, size2, {}, ans)
    print(str(ans[size1][size2])[1:-1].replace(",",""))
