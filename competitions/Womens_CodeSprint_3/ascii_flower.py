#https://www.hackerrank.com/contests/womens-codesprint-3/challenges/ascii-flower

def solution(r, c):
    ans = ""
    for i in range(r):
        row = ""
        for i in range(c):
            row += "..O.."
        row += "\n"
        for i in range(c):
            row += "O.o.O"
        row += "\n"
        for i in range(c):
            row += "..O.."
        row += "\n"
        ans += row
    ans = ans[:len(ans)-1]
    return ans

if __name__ == "__main__":
    r, c = [int(_) for _ in input().strip().split()]
    ans = solution(r, c)
    print(ans)
