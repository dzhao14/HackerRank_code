#https://www.hackerrank.com/challenges/camelcase

def solution(s):
    count = 1
    for char in s:
        if ord(char) <= 90:
            count += 1
    return count

if __name__ == "__main__":
    s = input().strip()
    ans = solution(s)
    print(str(ans))
