#https://www.hackerrank.com/contests/rookierank-3/challenges/comparing-times

from datetime import datetime

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        ts = input().split()
        t1 = datetime.strptime(ts[0], '%I:%M%p')
        t2 = datetime.strptime(ts[1], '%I:%M%p')
        if t1 < t2:
            print("First")
        else:
            print("Second")
