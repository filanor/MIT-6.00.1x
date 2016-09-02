#
#	pset1_2.py
#
#	filanor
#
#
#	Write a program that prints the number of times the string 'bob' occurs in s
#
#	For MIT 6.00.1x ProblemSet 1 Problem 2
#
#


rez = 0
for i in range(len(s)):
    if s[i: i+3] == 'bob':
        rez += 1
print("Number of times bob occurs is:", rez)