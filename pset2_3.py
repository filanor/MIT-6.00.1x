#
# program that calculates the minimum fixed monthly 
# payment needed in order pay off a credit card balance within 12 months.
# using Bisection Search
#
# input: balance - the outstanding balance on the credit card
#		 annualInterestRate - annual interest rate as a decimal
#

__autor__ = 'filanor'

balance = int(input('Please input balance:  '))
annualInterestRate = float(input('Please input annualInterestRate:  '))
min = balance / 12
max = (balance * (1 + annualInterestRate)**12) / 12

while True:
	# calculate new month payment
	monthPayment = round((min + max) / 2, 2)
	b = balance

	#calculate balance at the end of the year
	for x in range(0,12):
		unpaidBalance = b - monthPayment
		b = unpaidBalance + unpaidBalance * annualInterestRate / 12

		
	if abs(b) < 0.1:
		print('Lowest Payment:' + str(monthPayment))
		break
	elif b > 0:
		min = monthPayment
	elif b < 0:
		max = monthPayment





