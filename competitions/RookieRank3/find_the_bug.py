#https://www.hackerrank.com/contests/rookierank-3/challenges/find-the-bug

if __name__ == "__main__":
    n = int(input())
    r = -1
    c = -1
    for i in range(n):
        s = input()
        try:
            c = s.index("X")
            r = i
            print(str(r) + "," + str(c))
            break
        except:
            pass
