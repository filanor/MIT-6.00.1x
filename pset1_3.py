#
#   pset1_3.py
#
#	filanor
#
#	
#	This program prints the longest substring of s in which the letters occur in alphabetical order
#	Programm for MIT 6.00.1x ProblemSet Problem 3
#
#



s = "bnbzszofekp"
rez = ""
temp = ""
count = 0
rez_count = 0

for i in range(0, len(s)):
	if i == 0:
		temp = s[i]
		count = 1
	elif s[i] >= s[i - 1]:
		temp = temp + s[i]
		count += 1
	elif rez_count < count: 
		rez = temp
		rez_count = count
		count = 1
		temp = s[i]
	else:
		count = 1
		temp = s[i]
	if i == len(s) - 1 and count > rez_count:
		rez = temp


print("Longest substring in alphabetical order is:", rez)
