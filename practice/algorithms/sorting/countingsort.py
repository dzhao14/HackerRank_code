#https://www.hackerrank.com/challenges/countingsort4

#counting sort
if __name__ == '__main__':
    size = int(input().strip())
    zeros = [0 for i in range(100)]
    sums = [0 for i in range(100)]
    given = []
    for i in range(size):
        num, s = input().strip().split()
        num = int(num)
        zeros[num] += 1
        if i < size/2:
            s = "-"
        given.append((num, s))

    tot = 0
    for i in range(100):
        tot += zeros[i]
        sums[i] = tot

    output = [0 for i in range(len(given))]
    for i in given:
        output[sums[i[0]] - zeros[i[0]]] = i[1]
        zeros[i[0]] -= 1

    out = ""
    for i in output:
        out = out + i
        out = out + " "

    print(out.strip())
