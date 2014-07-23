## Find the area cost of tile based on sqft cost

intLength = 0
intWidth = 0
fltCost = 0

while True:
	try:
		intLength = int(input("What is the length of the area?"))
		intWidth = int(input("What is the width of the area?"))
		fltCost = float(input("what is the cost per square foot of tile?"))
	except ValueError:
		print("One or more value(s) was not a number...")
		continue
	else:
		break

print("$" + str(intWidth * intLength * fltCost) + " would be the cost")
