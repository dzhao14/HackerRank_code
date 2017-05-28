#https://www.hackerrank.com/contests/world-codesprint-11/challenges/simple-file-commands

import heapq

def create(file_names, s):
    name = s[4:]
    if name not in file_names:
        print("+ " + name)
        file_names[name] = [1]
    else:
        m = heapq.heappop(file_names[name])
        if m != 0:
            print("+ " + name +"(" + str(m) + ")")
        else:
            print("+ " + name)
        if len(file_names[name]) == 0:
            file_names[name].append(m+1)

def delete(file_names, s):
    name = s[4:]
    if "(" in name:
        lol = name.split("(")[1]
        m = int(lol.split(")")[0])
        heapq.heappush(file_names[name.split("(")[0]], m)
    else:
        heapq.heappush(file_names[name], 0)
    print("- " + name)

def rename(file_names, s):
    name1 = s[4:].split(" ")[0]
    if "(" in name1:
        lol = name1.split("(")[1]
        m = int(lol.split(")")[0])
        heapq.heappush(file_names[name1.split("(")[0]], m)
    else:
        heapq.heappush(file_names[name1], 0)
        
    name2 = s[4:].split(" ")[1]
    if name2 not in file_names:
        file_names[name2] = [1]
        print("r " + name1 + " -> " + name2)
    else:
        m = heapq.heappop(file_names[name2])
        if len(file_names[name2]) == 0:
            file_names[name2].append(m+1)
        if m != 0:
            print("r " + name1 + " -> " + name2 + "(" + str(m) + ")")
        else:
            print("r " + name1 + " -> " + name2)
    
    
def solution(q):
    file_names = {}
    for i in range(q):
        s = input().strip()
        if s[:3] == "crt":
            create(file_names, s)
        elif s[:3] == "del":
            delete(file_names, s)
        elif s[:3] == "rnm":
            rename(file_names, s)

if __name__ == "__main__":
    q = int(input())
    solution(q)
