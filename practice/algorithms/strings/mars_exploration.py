#https://www.hackerrank.com/challenges/mars-exploration

def solution(s):
    temp = 0
    count = 0
    for i in s:
        if temp % 3 == 0 or temp % 3 == 2:
            if i != "S":
                count += 1
        else:
            if i != "O":
                count += 1
        temp += 1
    return count
            

if __name__ == "__main__":
    s = input().strip()
    ans = solution(s)
    print(str(ans))
