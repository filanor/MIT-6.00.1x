#
#
# program that calculates the minimum fixed monthly 
# payment needed in order pay off a credit card balance within 12 months.
#
# input: balance - the outstanding balance on the credit card
#		 annualInterestRate - annual interest rate as a decimal
#


__autor__ = 'filanor'

def checkMinPayment(balance, annualInterestRate, value):
	'''
	function checks is value whether a sufficient amount
	'''
	for x in range(0,12):
		unpaidBalance = balance - value
		balance = unpaidBalance + unpaidBalance * annualInterestRate / 12
	if balance < 0:
		return True
	else:
		print('value = ' + str(value) + ' = false')
		return False 

def searchMinPayment(balance, annualInterestRate):
	'''
	function do linear search until find inimum fixed monthly payment
	step 10$
	'''

	minPayment = 0
	while checkMinPayment(balance, annualInterestRate, minPayment) == False:
		minPayment += 0.01
	return minPayment



balance = int(input('Please input balance:  '))
annualInterestRate = float(input('Please input annualInterestRate:  '))

min = searchMinPayment(balance, annualInterestRate)
print('Lowest Payment: ' + str(min))