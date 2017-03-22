#https://www.hackerrank.com/contests/101hack47/challenges/permutation-possibility

def solution(arr):
    hashtable = {}
    for i in arr:
        if i in hashtable:
            return "NO"
        else:
            hashtable[i] = True
    return "YES"

if __name__ == "__main__":
    size = input()
    arr = [int(_) for _ in input().strip().split()]
    ans = solution(arr)
    print(str(ans))
