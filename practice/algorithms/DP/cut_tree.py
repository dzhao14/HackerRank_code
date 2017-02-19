#https://www.hackerrank.com/challenges/cuttree?h_r=internal-search
#not solved
ans = 0

def solution(graph, start, memo):
    global ans
    for neib in graph[start]:
        count = 1
        key = (start, neib)
        if key in memo:
            continue
        memo[key] = sibling(graph, neib, start, k, memo)
        count += memo[key]
        print(count)
        if count >= k:
            ans += 1
    if count >= k:
        ans += 1

    return memo

def sibling(graph, neib, prev, k, memo):
    global ans
    count = 1
    if len(graph[neib]) == 1:
        if 1 >= k:
            ans += 1
        return count
    for neib2 in graph[neib]:
        key = (neib, neib2)
        if neib2 == prev:
            continue
        memo[key] = sibling(graph, neib2, neib, k, memo)
        count += memo[key]
        if count >= k:
            ans += 1
    return count

if __name__ == "__main__":
    ans = 0
    n, k = [int(t) for t in input().strip().split()]
    graph = {}
    for i in range(n-1):
        u, v = [int(t) for t in input().strip().split()]
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]
        memo = {}
        memo = solution(graph, 1, memo)
        print(str(ans))
