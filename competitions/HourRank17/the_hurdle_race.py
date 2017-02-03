#https://www.hackerrank.com/contests/hourrank-17/challenges/the-hurdle-race

def solution(arr, height):
    count = 0
    for i in arr:
        if i <= height:
            pass
        else:
            count += i - height
            height += i - height
    return count
        

if __name__ == "__main__":
    size, height = [int(temp) for temp in input().strip().split()]
    arr = [int(temp) for temp in input().strip().split()]

    ans = solution(arr, height)
    print(str(ans))
