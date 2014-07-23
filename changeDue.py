## Find the change quanta for an amount and a given $$

fltAmountDue, fltCashGiven, intPennies, intNickels, intDimes, intQuarters, intDollars, intFives, intTens, \
              intTwenties, intFifties, intHundreds = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

bolAllocated = False
while True:
	try:
		fltAmountDue = float(input("What's the cost?"))
		fltCashGiven = float(input("How much did you pay?"))
	except ValueError:
		print("One or more value(s) was not a number...")
		continue
	else:
		break

fltRemainder = float(fltCashGiven - fltAmountDue)
if fltCashGiven < fltAmountDue:
	print("...i think you might need more monetary investment to make this a legal transaction.")

while not fltRemainder == 0:
	bolOnceThrough = False
	if fltRemainder == 0:
		bolAllocated = True
		break
	elif fltRemainder >= 100:
		intHundreds += 1
		fltRemainder -= 100
		bolOnceThrough = True
	elif fltRemainder >= 50 and bolOnceThrough == False:
		intFifties += 1
		fltRemainder -= 50
	elif fltRemainder >= 20 and bolOnceThrough == False:
		intTwenties += 1
		fltRemainder -= 20
		bolOnceThrough = True
	elif fltRemainder >= 10 and bolOnceThrough == False:
		intTens += 1
		fltRemainder -= 10
		bolOnceThrough = True
	elif fltRemainder >= 5 and bolOnceThrough == False:
		intFives += 1
		fltRemainder -= 5
		bolOnceThrough = True
	elif fltRemainder >= 1 and bolOnceThrough == False:
		intDollars += 1
		fltRemainder -= 1
		bolOnceThrough = True
	elif fltRemainder >= .25 and bolOnceThrough == False:
		intQuarters += 1
		fltRemainder -= .25
		bolOnceThrough = True
	elif fltRemainder >= .1 and bolOnceThrough == False:
		intDimes += 1
		fltRemainder -= .1
		bolOnceThrough = True
	elif fltRemainder >= .05 and bolOnceThrough == False:
		intNickels += 1
		fltRemainder -= .05
		bolOnceThrough = True
	elif fltRemainder >= .01 and bolOnceThrough == False:
		intPennies += 1
		fltRemainder -= .01
	elif fltRemainder < .01:
		break

print("After $" + str(round(float(fltCashGiven), 2)) + " is given to pay for $" + str(round(fltAmountDue,2)) + ", the breakup is as follows:")
print("100's - " + str(intHundreds) + "\n50's - " + str(intFifties) + "\n20's - " + str(intTwenties) + "\n10's - " + \
      str(intTens) + "\n5's - " + str(intFives) + "\n1's - " + str(intDollars) + "\nQuarters - " + str(intQuarters) + \
      "\nDimes - " + str(intDimes) + "\nNickels - " + str(intNickels) + "\nPennies - " + str(intPennies))
