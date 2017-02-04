#https://www.hackerrank.com/challenges/sherlock-and-valid-string

def solution(s):
    count = [0 for i in range(26)]
    for char in s:
        count[ord(char) - 97] += 1

    idx = 0
    while True:
        if idx >= len(count):
            break
        if count[idx] == 0:
            del count[idx]
        else:
            idx += 1

    totSum = sum(count)
    if count[1:] == count[:-1]:
        return "YES"
    val = count[0]
    if val * len(count) == totSum - 1:
        return "YES"
    if (val-1) * len(count) == totSum -1:
        return "YES"

    seenOnce = False
    for i in count:
        if i == 1 and seenOnce == False:
            seenOnce = True
        elif i == 1 and seenOnce == True:
            seenOnce = False
            break
    if seenOnce == True:
        return "YES"
        

    return "NO"

if __name__ == "__main__":
    s = input().strip()
    ans = solution(s)
    print(ans)
