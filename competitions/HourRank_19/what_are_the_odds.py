#https://www.hackerrank.com/contests/hourrank-19/challenges/what-are-the-odds

def solution(arr):
    count = 1
    for i in range(len(arr)):
        x = 0
        for val in range(i, len(arr)):
            x = x^arr[val]
            if x <= 0:
                count += 1

    return count
                    

if __name__ == "__main__":
    piles = int(input())
    arr = [int(_) for _ in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
