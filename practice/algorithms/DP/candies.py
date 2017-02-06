#https://www.hackerrank.com/challenges/candies
#not solved

def solution(arr, ans):
    for i in range(len(arr)):
        if i == 0:
            ans[0] = 1
        else:
            if arr[i-1] > arr[i] and ans[i-1] == 1:
                ans[i] = 1
                for j in range(i-1,-1,-1):
                    if ans[j] == ans[j+1]:
                        ans[j] += 1
                    else:
                        break
            elif arr[i-1] < arr[i]:
                ans[i] = ans[i-1] + 1
            else:
                ans[i] = 1
    return ans

if __name__ == "__main__":
    size = int(input())
    arr = []
    for i in range(size):
        n = int(input())
        arr.append(n)
    ansR = [0 for i in range(size)]
    ans = sum(solution(arr, ansR))
    print(str(ans))
