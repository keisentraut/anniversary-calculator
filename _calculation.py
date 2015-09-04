#!/usr/bin/python

from anniversary import isInterestingNumberOfDays, isInterestingNumberOfMonths
import sys

if len(sys.argv) != 3:
	print("usage: %s 0 30000" % sys.argv[0])
	sys.exit(1)

start = int(sys.argv[1])
end = int(sys.argv[2])

if start >= end:
	print("first argument %u must be smaller then second %u" % (start,end))
	sys.exit(1)

d,m,y=0,0,0
for i in range(start, end):
	if i%365 == 0: y += 1
	if i%30 == 0 and isInterestingNumberOfMonths(i/30): m += 1
	if isInterestingNumberOfDays(i): d+=1

n = end - start
t = d+m+y
if d!=0: print("%4u interesting years   (one every %d days)" % (y, n/y) )	
if m!=0: print("%4u interesting months  (one every %d days)" % (m, n/m) )	
if y!=0: print("%4u interesting days    (one every %d days)" % (d, n/d) )	
if t!=0: print("%4u interesting events  (one every %d days)" % (t, n/t) ) 

