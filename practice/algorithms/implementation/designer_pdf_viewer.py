#https://www.hackerrank.com/challenges/designer-pdf-viewer

def solution(heights, s):
    w = len(s)
    h = 1
    for i in s:
        if heights[ord(i)-97] > h:
            h = heights[ord(i)-97]
    return w * h

if __name__ == "__main__":
    heights = [int(temp) for temp in input().strip().split()]
    s = input().strip()
    ans = solution(heights, s)
    print(str(ans))
