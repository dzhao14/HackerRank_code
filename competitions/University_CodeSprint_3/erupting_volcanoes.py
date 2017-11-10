#https://www.hackerrank.com/contests/university-codesprint-3/challenges/erupting-volcanoes

def solution(n, volcanoes):
    count = 0
    for row in range(n):
        for col in range(n):
            val = 0
            for volcano in volcanoes:
                val += max(0,volcano[2]-max(abs(volcano[0]-row), abs(volcano[1]-col)))
            count = max(val, count)
    return count

def solution2(n, volcanoes):
    count = 0
    for row in range(n):
        for col in range(n):
            val = 0
            for key, w in volcanoes.items():
                y = key % n
                x = (key - y) // n
                val += max(0, w-max(abs(x-row), abs(y-col)))
            count = max(val, count)
    return count
                

def read_input(n):
    volcanoes = []
    for _ in range(m):
        x, y, w = [int(_) for _ in input().strip().split()]
        volcanoes.append([x, y, w])
    return volcanoes

def read_input2(n):
    volcanoes = {}
    for _ in range(m):
        x, y, w = [int(_) for _ in input().strip().split()]
        key = n * x + y
        if key in volcanoes:
            volcanoes[key] += w
        else:
            volcanoes[key] = w
    return volcanoes
    

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    volcanoes = read_input2(n)
    
    ans = solution2(n, volcanoes)
    print(str(ans))
