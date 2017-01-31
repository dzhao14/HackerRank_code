#https://www.hackerrank.com/contests/world-codesprint-9/challenges/weighted-uniform-string

letter_weight_dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
                     "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
                     "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
                     "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
                     "z": 26}

def splitStrings(s):
    out = {}
    temp = ""
    val = 0
    for c in s:
        if c == temp:
            val += letter_weight_dic[c]
        else:
            temp = c
            val = letter_weight_dic[c]
        out[val] = True
    out.pop("", None)
    return out

if __name__ == '__main__':
    s = input()
    queries = int(input())
    weights = []
    for i in range(0, queries):
        weight = int(input())
        weights.append(weight)
    uniform_weights = splitStrings(s)
    for n in weights:
        if n in uniform_weights:
            print("Yes")
        else:
            print("No")
