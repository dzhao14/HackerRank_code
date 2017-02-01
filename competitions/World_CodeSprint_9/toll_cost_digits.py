#https://www.hackerrank.com/contests/world-codesprint-9/challenges/toll-cost-digits

#not solved

# equivalent to (-n) % 10
def flip(n):
    if 10 - n == 10:
        return 0
    return 10 - n

def calculatePaths(graph, weights, out):
    for x in graph:
        for y in graph:
            if x == y:
                continue
            elif (x, y) in weights:
                continue
            else:
                seen = {}
                seen[x] = True
                for neib in graph[x]:
                    DFS(x, neib, y, graph, weights, out, seen, weights[(x, neib)])

    paths = []
    for x in range(10):
        paths.append(0)
    for key in out:
        for d in out[key]:
            paths[d] += 1
    return paths

def DFS(s, x, y, graph, weights, out, seen, w):
    seen[x] = True
    if x == y:
        print("this should never happen")
    elif (x, y) in weights:
        for d in w:
            weights[(s, y)] = {}
            weights[(s, y)][d] = True
            out[y][d] = 1
    else:
        for neib in graph[x]:
            if neib in seen:
                pass
            else:
                DFS(s, neib, y, graph, weights, out, seen, weights[(x, neib)])
    
    
if __name__ == "__main__":
    graph = {}
    weights = {}
    out = {}
    size_graph = input()
    size_graph = size_graph.split()
    cities = int(size_graph[0])
    roads = int(size_graph[1])
    for i in range(roads):
        road = input()
        road = road.split()
        x = int(road[0])
        y = int(road[1])
        r = int(road[2])
        d = r % 10
        if (x, y) in weights and d in weights:
            continue
        
        if x not in graph:
            out[x] = {}
            graph[x] = {}
            graph[x][y] = True
            out[x][d] = 1
        else:
            graph[x][y] = True
            out[x][d] = 1

        if y not in graph:
            out[y] = {}
            graph[y] = {}
            graph[y][x] = True
            out[y][flip(d)] = 1
        else:
            out[y][flip(d)] = 1
            graph[y][x] = True
            
        if (x, y) not in weights:
            weights[(x, y)] = {}
            weights[(x, y)][d] = True
        else:
            weights[(x, y)][d] = True
        if (y, x) not in weights:
            weights[(y, x)] = {}
            weights[(y, x)][flip(d)] = True
        else:
            weights[(y, x)][flip(d)] = True

    paths = calculatePaths(graph, weights, out)

    for path in paths:
        print(path)
    
    
