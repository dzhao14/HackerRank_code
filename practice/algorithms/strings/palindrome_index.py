#https://www.hackerrank.com/challenges/palindrome-index
#not solved

#O(n^2) is too slow
def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def solution(s):
    if isPalindrome(s):
        return -1
    for i in range(len(s)):
        newS = s[:i] + s[i+1:]
        if isPalindrome(newS):
            return i
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        ans = solution(s)
        print(str(ans))
