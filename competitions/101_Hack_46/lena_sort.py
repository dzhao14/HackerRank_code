#https://www.hackerrank.com/contests/101hack46/challenges/lena-sort
#not even close to being solved ugh

def solution(l, c, memo):
    ans = [-1] * l
    memo[(1,0)] = 0
    memo[(2,1)] = 1
    memo[(3,2)] = 1
    memo[(3,3)] = 0
##    for i in range(pow(10,7)):
##        memo[(1,i)] = -1

    for l in range(3, l+1):
        for c in range(l*(l-1)//2, -1, -1):
            if c - (l-1) <= 0:
                break
            for a in range(l-1):
                brk = False
                if brk:
                    break
                for b in range(c-(l-1),-1,-1):
                    if (l-1-a, c - (l-1)- b) in memo and (a,b) in memo: 
                        #do offsets to ans
                        memo[(l, c)] = a
                        brk = True
                        break
    return
                    
                    
if __name__ == "__main__":
    q = int(input())
    memo = {}
    for i in range(q):
        l, c = [int(t) for t in input().strip().split()]
        ans = solution(l, c, memo)
##        print(str(ans)[1:-1].replace(",",""))
        
    
