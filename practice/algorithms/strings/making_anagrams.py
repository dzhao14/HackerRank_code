#https://www.hackerrank.com/challenges/making-anagrams

def solution(a, b):
    ar = [0 for i in range(26)]
    br = [0 for i in range(26)]
    for i in a:
        ar[ord(i)-97] += 1
    for i in b:
        br[ord(i)-97] += 1
    count = 0
    for i in range(26):
        count += abs(ar[i] - br[i])
    return count

if __name__ == "__main__":
    a = input().strip()
    b = input().strip()
    ans = solution(a, b)
    print(str(ans))
