#https://www.hackerrank.com/challenges/string-reduction
#not solved

def swap(seq, idx):
    first = seq[idx]
    second = seq[idx + 1]
    if first == "a" or second == "a":
        if first == "b" or second == "b":
            return "c"
        else:
            return "b"
    else:
        return "a"

def solution(seq, idx, memo):
    key = seq
    if key in memo:
        return memo[seq]
    if idx >= len(seq) -1:
        return len(seq)
    if seq[idx] == seq[idx+1]:
        memo[key] = solution(seq, idx + 1, memo)
        return memo[key]

    memo[key] = min(solution(seq[:idx] + swap(seq, idx) + seq[idx+2:],
               0, memo), solution(seq, idx + 1, memo))
    return memo[key]
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        seq = input().strip()
        ans = solution(seq, 0, {})
        print(str(ans))
