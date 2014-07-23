## Find the area cost of tile based on sqft cost

fltLength = 0
fltWidth = 0
fltCost = 0

while True:
	try:
		fltLength = float(input("What is the length of the area?"))
		fltWidth = float(input("What is the width of the area?"))
		fltCost = float(input("what is the cost per square foot of tile?"))
	except ValueError:
		print("One or more value(s) was not a number...")
		continue
	else:
		break

print("$" + str( round( float(fltWidth * fltLength * fltCost) , 2)) + " would be the cost")
