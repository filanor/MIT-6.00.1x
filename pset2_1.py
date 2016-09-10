# Paste your code into this box

#balance = int(input("Please input your balance: "))
#annualInterestRate = float(input('Please input annual interest rate as a decimal'))
#monthlyPaymentRate = float(input('Please input minimum monthly payment rate as a decimal'))


def balanceAfterYear(balance, annualInterestRate, monthlyPaymentRate):
	'''
	this function calculate balance after year
	'''
	for mounth in range(0, 12):
		balance = updateBalance(balance, annualInterestRate, monthlyPaymentRate)
	return balance

def updateBalance(balance, annualInterestRate, monthlyPaymentRate):
	'''
	this function update balabne after each month
	output: balance at the end of the month
	'''

	# calculate unpaid balance
	unpaidBalance = balance - balance * monthlyPaymentRate
	#calculate balance in the end of month
	balance = unpaidBalance + unpaidBalance * ( annualInterestRate / 12)
	return balance


#calculate and print balance after year
balance = round(balanceAfterYear(balance, annualInterestRate, monthlyPaymentRate), 2)
print('Remaining balance: ' + str(balance))