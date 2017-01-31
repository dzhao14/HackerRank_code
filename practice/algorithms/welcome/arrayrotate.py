#!/bin/python3

import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

qs = []
for a0 in range(q):
    m = int(input().strip())
    qs.append(m)

newa = []
k = k % n
for i in range(len(a)-k, len(a)):
    newa.append(a[i])
for i in range(len(a) - k):
    newa.append(a[i])

for m in qs:
    print(newa[m])
