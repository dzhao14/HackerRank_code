#https://www.hackerrank.com/challenges/strange-advertising

def solution(n):
    seen = 0
    sent = {}
    sent[-1] = 5
    for i in range(n):
        sent[i] = (sent[i-1] // 2) * 3
        seen += sent[i-1] // 2
    return seen

if __name__ == "__main__":
    n = int(input())
    ans = solution(n)
    print(str(ans))
