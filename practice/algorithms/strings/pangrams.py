#https://www.hackerrank.com/challenges/pangrams

def solution(s):
    if "a" not in s and "A" not in s:
        return "not pangram"
    if "b" not in s and "B" not in s:
        return "not pangram"
    if "c" not in s and "C" not in s:
        return "not pangram"
    if "d" not in s and "D" not in s:
        return "not pangram"
    if "e" not in s and "E" not in s:
        return "not pangram"
    if "f" not in s and "F" not in s:
        return "not pangram"
    if "g" not in s and "G" not in s:
        return "not pangram"
    if "h" not in s and "H" not in s:
        return "not pangram"
    if "i" not in s and "I" not in s:
        return "not pangram"
    if "j" not in s and "J" not in s:
        return "not pangram"
    if "k" not in s and "K" not in s:
        return "not pangram"
    if "l" not in s and "L" not in s:
        return "not pangram"
    if "m" not in s and "M" not in s:
        return "not pangram"
    if "n" not in s and "N" not in s:
        return "not pangram"
    if "o" not in s and "O" not in s:
        return "not pangram"
    if "p" not in s and "P" not in s:
        return "not pangram"
    if "q" not in s and "Q" not in s:
        return "not pangram"
    if "r" not in s and "R" not in s:
        return "not pangram"
    if "s" not in s and "S" not in s:
        return "not pangram"
    if "t" not in s and "T" not in s:
        return "not pangram"
    if "u" not in s and "U" not in s:
        return "not pangram"
    if "v" not in s and "V" not in s:
        return "not pangram"
    if "w" not in s and "W" not in s:
        return "not pangram"
    if "x" not in s and "X" not in s:
        return "not pangram"
    if "y" not in s and "Y" not in s:
        return "not pangram"
    if "z" not in s and "Z" not in s:
        return "not pangram"
    return "pangram"
if __name__ == "__main__":
    s = input().strip()
    ans = solution(s)
    print(ans)
