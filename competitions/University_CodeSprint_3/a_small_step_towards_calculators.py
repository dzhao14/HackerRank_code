#https://www.hackerrank.com/contests/university-codesprint-3/challenges/a-small-step-toward-calculators

def solution(s):
    if "+" in s:
        print(int(s[0]) + int(s[2]))
    else:
        print(int(s[0]) - int(s[2]))

if __name__ == "__main__":
    s = input()
    solution(s)
