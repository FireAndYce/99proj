## Prime factorization

result = ""
while True:
	try:
		i = int(input("What is your number?"))
	except ValueError:
		print("that is not an integer")
		continue
	else:
		break

s = 1
while s <= round(i/2):
	s+= 1
	if (i % s) == 0:
		result += str(s) + ","
		i = i/s
		s = 1
		
print(result + str(int(i)))
