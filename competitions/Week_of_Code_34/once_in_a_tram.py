#https://www.hackerrank.com/contests/w34/challenges/once-in-a-tram

if __name__ == "__main__":
    n = int(input())
    n += 1
    while n <= 999999:
        sum1 = sum([int(i) for i in str(n)[:3]])
        sum2 = sum([int(i) for i in str(n)[3:]])
        if sum1 == sum2:
            break
        else:
            n += 1
    print (str(n))
