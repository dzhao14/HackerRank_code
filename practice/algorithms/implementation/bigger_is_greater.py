#https://www.hackerrank.com/challenges/bigger-is-greater
#not solved

from itertools import permutations

def solution(s):
    arr = [ord(i) for i in s]
    a = permutations(arr)
    b = a.__next__()
    try:
        out = a.__next__()
        outs = [chr(i) for i in out]
        return str(outs)#[1:-1].replace(" ","").replace(",","").replace("\'","")
    except:
        return "no answer"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        ans = solution(s)
        print(str(ans)[1:-1].replace(",","").replace(" ","").replace("\'",""))
