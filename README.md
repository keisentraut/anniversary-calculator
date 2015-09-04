# anniversary-calculator
never forget birthdays, anniversaries or the day when you will be 12345 days old!
```
$ ./anniversary.py 10
anniversaries from 2015-09-05 to 2015-09-14:
--------------------------------------------

Wednesday, 09.09.2015 (+ 4 days)
--------------------------------
678 days   - first day at Example Company

Friday, 11.09.2015 (+ 6 days)
-----------------------------
  6 years  - first day at school
 14 years  - WTC attacks (9/11)
```
I use this script in combination with a daily cronjob, which sends me the output per email 
once in the morning at 03:00am. You can use it for birthdays, your wedding anniversary or
just random history dates.

# FAQs

## How can I add actually important dates?
It's quite easy. Just update take a look at the data/example.txt file, it should
be pretty self-explanatory:
```
# This is an example file for anniversary.py
# Just remove this file, and add your own important days!
#
# the required format should be pretty straightforward:
# YYYY-MM-DD + space + arbitrary text
#
# all lines with starting with a '#' sign are ignored
# empty lines are ignored, too
# this line is ignored, too, because leading/trailing whitespace is removed

# family birthdays
1971-01-22 mother
1970-02-23 father
1950-03-24 grandma #1
1947-04-25 grandpa #1
1947-05-26 grandma #2
1947-06-27 grandpa #2
1990-05-26 big sister
1992-06-27 big brother (a.k.a NSA)
1994-07-28 me 
1996-08-29 small brother
	
# important milestones in my life
2009-09-11 first day at school
2012-09-30 graduated at university
2013-10-31 first day at Example Company

# other events
2000-01-01 millenium
2001-09-11 WTC attacks (9/11)
```

If you want to have more than one files, just change the FILES global variable in anniversary.py.
You might want to use absolute paths instead of relative paths like in the example.

## How many output will I get, if I add N dates?
Use the _calculatiion.py script for that:
```
$ ./_calculation.py 0 30000  
  83 interesting years   (one every 361 days)
  44 interesting months  (one every 681 days)
  91 interesting days    (one every 329 days)
 218 interesting events  (one every 137 days)
```

So you if you only add dates which are equally distributed in the timespan between today and the day 30000 days ago,
you can expect N/137 lines of output.

## Which numbers are considered "interesting"?
Use the provided script "_displayInterestingNumbers.py":

```
$ ./_displayInterestingNumbers.py
11
22
33
[...snip...]
543
555
567
[...snip...]
99999999999
```

## I don't agree with the "interesting numbers"!
No problem, just modify the following 3 functions in "anniversary.py":
```
def isInterestingNumberOfYears(n):
def isInterestingNumberOfMonths(n):
def isInterestingNumberOfDays(n):
```

## Do I need Python2/3, Windows/Linux?
It should work with all combinations, though I'm using Python 3 on Linux.

## But Python is using the Gregorian calendar which is not valid before 1582!
I don't f***ing care.

## What licence does this code have?
The WTFPL ;) http://www.wtfpl.net/

