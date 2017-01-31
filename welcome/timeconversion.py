#!/bin/python3

import sys


time = input().strip()
end = time[8:]
hh = int(time[:2])
mm = int(time[3:5])
ss = int(time[6:8])

if end == "AM" and hh == 12:
    hh = 0
if end == "PM" and hh != 12:
    hh = hh + 12
    
print(str(hh).zfill(2)+":"+str(mm).zfill(2)+":"+str(ss).zfill(2))
