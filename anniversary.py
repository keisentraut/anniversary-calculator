#!/usr/bin/env python
#

import datetime
import sys

PATH = "./data/" # must have trailing /
FILES = ["example.txt",] # feel free to add more files, if you like!
INPUTFORMAT = "%Y-%m-%d"
OUTPUTFORMAT = "%A, %d.%m.%Y"

###############################################################################
###############################################################################
###############################################################################
def usage():
	# print usage
	print("ANNIVERSARY CALCULATOR - klaus (dot) eisentraut (at) mailbox.org")
	print("")
	print("Usage examples:")
	print("%s              # calculate for today plus 4 following days " % sys.argv[0])
	print("%s 2015-12-31   # calculate for given day plus 4 following days" % sys.argv[0])
	print("%s 7            # calculate for today plus 6 following days " % sys.argv[0])
	print("%s 2015-12-31 7 # calculate for given day plus 6 following days" % sys.argv[0])
	sys.exit(1)

# calculate an number of "interesting" numbers 
# only numbers with 10 or less digits
def generateInterestingSet():
	ret = set()
	# first add numbers like 11, 44444, 333, ... 
	tmp = 1 
	for length in range(1,11):
		tmp = tmp*10 + 1
		ret |= set(digit*tmp for digit in range(1,10))
	# now add numbers where the digits are decreasing continously!
	# e.g. 7654, 987654, 3210, ...
	# 3 digits minimum length, because 54 is not really "interesting"
	for length in range(3,11):
		for startDigit in range(length-1,10):
			tmp = 0
			for digit in range(startDigit, startDigit-length, -1):
				tmp = tmp*10 + digit
			ret.add(tmp)
	# now the same as above, but with increasing numbers.
	# e.g. 789, 123456, 67890
	# again, 3 digits minimum length, because 67 is not really "interesting"
	for length in range(3,11):
		for startDigit in range(1, 12-length):
			tmp = 0
			for digit in range(startDigit, startDigit+length):
				tmp = tmp*10 + (digit%10) # in the last round, d can be 10
			ret.add(tmp)
	return ret

interestingNumbers = generateInterestingSet()

def isInterestingNumberOfYears(n):
	# a birthday is always special, we want to include all of them
	return True 


def isInterestingNumberOfMonths(n):
	if n % 100 == 0: return True
	if n in interestingNumbers: return True	
	return False

def isInterestingNumberOfWeeks(n):
	if n % 100 == 0: return True
	if n in interestingNumbers: return True	
	return False

def isInterestingNumberOfDays(n):
	if n % 1000 == 0: return True
	if n in interestingNumbers: return True
	return False

###############################################################################
###############################################################################
###############################################################################

def underline(s):
	return s + "\n" + ("-"*len(s)) + "\n"

def str2date(s):
	return datetime.datetime.strptime(s, INPUTFORMAT).date()	

def date2str(d):
	return datetime.datetime.strftime(d, OUTPUTFORMAT)

def isleap(n):
	if n%400: return True
	if n%100: return False
	if n%4: return True
	return False

# return length in days of month/year
def monthLength(month, year):
	if month == 2:
		if isleap(year):
			return 29
		else:
			return 28
	if month in {1,3,5,7,8,10,12}:
		return 31
	return 30

def interestingYear(bdate, now):
	age = None
	# normally, you have birthday, if it's the same day
	if bdate.day == now.day and bdate.month == now.month:
		age = now.year - bdate.year
	# except, if you are born on 29.2 and it is a leapyear
	elif bdate.day == 29 and bdate.month == 2 and now.day == 1 and now.month == 3 and not calendar.isleap(now.year):
		age = now.year - bdate.year
	if age != None and isInterestingNumberOfYears(age):
		return age
	return None

def interestingMonth(bdate, now):
	months = None
	# easy case, but this will not catch all dates where you get one month older!
	# often the current month is "too short" and you get 1 month older on the 1. of the next month instead
	# this happens when you are born on e.g. 31.12, 
	# then you'll get a month older at 31.01, 1.3, 31.3, 1.5, 31.5 ...
	if bdate.day == now.day:
			months = (now.year - bdate.year)*12 + (now.month - bdate.month)

	# so if it's actually the first, we have to look, if the last month was "long enough"
	elif now.day == 1:	
		yesterday = now - datetime.timedelta(1)
		lengthOfLastMonth = monthLength(yesterday.month, yesterday.year)
		# was the last month "too short"?
		if bdate.day > lengthOfLastMonth:
			months = (now.year - bdate.year)*12 + (now.month - bdate.month) - 1
	
	# finally, even if we got 1 month older exactly at "now", 
	# it still may be an uninteresting number of months...					
	if months != None and isInterestingNumberOfMonths(months):
		return months
	return None
	
def interestingDay(bdate, now):
	days = (now - bdate).days
	if isInterestingNumberOfDays(days):
		return days
	return None

def interestingWeek(bdate, now):
	days = (now - bdate).days
	if days%7 == 0:
		weeks = days/7
		if isInterestingNumberOfWeeks(weeks):
			return weeks
	return None

###############################################################################
###############################################################################
###############################################################################

if __name__ == "__main__":
	# parse command line options		
	today = datetime.date.today()
	nrFollowingDays = 5 # default is 5, i.e. today plus 4 following days!	
	if len(sys.argv) > 3:
		usage()
	try:
		if len(sys.argv) == 2:
			if '-' in sys.argv[1]: # date given
				today = datetime.datetime.strptime(sys.argv[1], INPUTFORMAT).date()
			else: # assume number was given
				nrFollowingDays = max(int(sys.argv[1]), 1)
		if len(sys.argv) == 3:
			today = datetime.datetime.strptime(sys.argv[1], INPUTFORMAT).date()
			# minimum value is 1 (only today)
			nrFollowingDays = max(int(sys.argv[2]), 1)
	except ValueError: # happens if the argument with '-' is not a valid date
		usage()

	# read files
	lines = [] 
	for f in FILES:
		# read current file linewise into tmp, ignore trailing/ending whitespace
		tmp = [ line.strip() for line in open(PATH + f) ]
		# add lines which are not empty and do not start with '#'
		lines += list(t for t in tmp if t and t[0]!='#')

	# example values: [[date(1945,05,08), "end of WW2"], ..., [date(2001,09,11), "WTC 9/11"]]
	birthdays = [[str2date(l.split(" ",1)[0]), l.split(" ",1)[1] ] for l in lines] 

	outputBuffer = ""
	for i in range(0,nrFollowingDays):
		daybuffer = ""
		# go through all saved dates and output, if they have something interesting
		# first for the years, then for days, and then for months (because months are the least interesting IMHO)
		for b in birthdays:
			years = interestingYear(b[0], today)
			if years != None:
				daybuffer += ("%5u years  - %s\n" % (years, b[1]))
		for b in birthdays:
			days = interestingDay(b[0], today)	
			if days != None:
				daybuffer += ("%5u days   - %s\n" % (days, b[1]))
		for b in birthdays:
			weeks = interestingWeek(b[0], today)	
			if weeks != None:
				daybuffer += ("%5u weeks  - %s\n" % (weeks, b[1]))
		for b in birthdays:
			months = interestingMonth(b[0], today)
			if months != None:
				daybuffer += ("%5u months - %s\n" % (months, b[1]))		
		# do we have output at all for this day? If not, we can skip it completly		
		if daybuffer != "":
			datestr = date2str(today)
			if not i==0:
				datestr += " (+%2u days)" % i
			outputBuffer += "\n" + underline(datestr)
			outputBuffer += (daybuffer)
		# finally, increment today by one to tomorrow
		today = today + datetime.timedelta(1)

	# reset today to what it was before we looped through the days...
	today = today - datetime.timedelta(nrFollowingDays)

	# was there at least one day with output at all?
	if outputBuffer == "":
		outputBuffer = "no anniversary from %s to %s\n" % (today, today + datetime.timedelta(nrFollowingDays-1))
	else:
		outputBuffer = underline("anniversaries from %s to %s:" % (today, today + datetime.timedelta(nrFollowingDays-1))) + outputBuffer

	sys.stdout.write(outputBuffer)


