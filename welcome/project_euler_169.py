import copy
import math
from itertools import zip_longest

#Attempt3 (flawed)
#Was going to use dp on this but it turned out that it doesn't work
dic3 = {}
seen={}
def f3(n):
    binN = bin(n)[2:]
    binArr =[]
    for n in binN:
        binArr.append(int(n))

    return f3_help(binArr)

def f3_help(binArr):
    out = []
    if len(binArr) == 1:
        return [binArr]
    low = binArr[math.ceil(len(binArr)/2):]
    high = binArr[:math.ceil(len(binArr)/2)]
    hout = f3_help(high)
    lout = f3_help(low)
    for x in hout:
        for y in lout:
            out.append(x+y)
    for y in lout:
        if y[0] == 0:
            for x in hout:
                if x[len(x)-1] != 0:
                    llow = copy.deepcopy(y)
                    hhigh = copy.deepcopy(x)
                    out = out + merge(hhigh, llow)
    return out

def merge(high, low):
    high[len(high)-1] = high[len(high)-1]-1
    low[0] = 2
    binArr = high + low
    return f3_help(binArr)
    

#Attempt2 (slow)
# bad use of DP
f2_dic = {}
def f2(n):
    binN = bin(n)[2:]
    binArr =[]
    for n in binN:
        binArr.append(int(n))

    return f2_help(binArr, 0)

def f2_help(binArr, ii):
    key = ''.join(str(binArr))
    key = key+str(ii)
    if key in f2_dic:
        return f2_dic[key]
    
    tempArr = copy.deepcopy(binArr)
    if ii >= len(binArr)-1:
        out = [binArr]
        f2_dic[key] = out
        return out
    elif binArr[ii] == 1 and binArr[ii+1] == 0:
        tempArr[ii] = 0
        tempArr[ii+1] = 2
        out = f2_help(tempArr, ii+1) + f2_help(binArr, ii+2) + f2_hh(tempArr, ii-1)
        f2_dic[key] = out
        return out
    elif binArr[ii] == 2 and binArr[ii+1] == 0:
        tempArr[ii]=1
        tempArr[ii+1]=2
        out = f2_help(tempArr, ii+1) + f2_help(binArr, ii+2)
        f2_dic[key] = out
        return out
    else:
        out = f2_help(binArr, ii+1)
        f2_dic[key] = out
        return out

def f2_hh(binArr, ii):
    key = ''.join(str(binArr))
    key = key+str(ii)
    if key in f2_dic:
        return f2_dic[key]
    
    tempArr = copy.deepcopy(binArr)
    if ii < 0:
        out = []
        f2_dic[key] = out
        return out
    elif binArr[ii] == 0:
        out = []
        f2_dic[key] = out
        return out
    elif binArr[ii] == 1:
        tempArr[ii] = 0
        tempArr[ii+1] = 2
        out = f2_help(tempArr, ii+1) + f2_hh(tempArr, ii-1)
        f2_dic[key] = out
        return out
    else:
        tempArr[ii] = 1
        tempArr[ii+1] = 2
        out = f2_help(tempArr, ii+1)
        f2_dic[key] = out
        return out

#Attempt 1 (super slow)
def f1(n):
    out = []
    for i in range(0, math.floor(n/2) + 1):
        j = n-i
        
        binI = bin(i)
        binJ = bin(j)
        temp = []
        for x, y in zip_longest(binI[::-1][:len(binI)-2],
                                binJ[::-1][:len(binJ)-2], fillvalue=0):
                                temp.append(int(x) + int(y))
        if temp not in out:
            out.append(temp)
    return out

#https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p169.py
ways = {}
def compute(n):
	ans = count_ways(n, n.bit_length() - 1, 2)
	return ans

def count_ways(number, exponent, repetitions):
    binNum = bin(number)[2:]
    key = (binNum, exponent, repetitions)
    print(key)
    if key not in ways:
        if exponent < 0:
            result = 1 if number == 0 else 0
        else:
            result = count_ways(number, exponent - 1, 2)
            power = 1 << exponent
            upper = power * (repetitions + 2)
            if repetitions > 0 and power <= number < upper:
            	result += count_ways(number - power, exponent, repetitions - 1)
        ways[key] = result
    return ways[key]
