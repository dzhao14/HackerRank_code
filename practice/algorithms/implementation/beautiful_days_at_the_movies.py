#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

def solution(i, j, k):
    count = 0
    for x in range(i, j+1):
        s = str(x)[::-1]
        dif = abs(x-int(s))
        if dif % k == 0:
            count += 1
    return count

if __name__ == "__main__":
    i, j, k = [int(t) for t in input().strip().split()]
    ans = solution(i, j, k)
    print(str(ans))
