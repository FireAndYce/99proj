##  Finding prime numbers

i = 1
f = 1
ui = input("type any key(s) and enter to stop...")

while True:
	i += 1
	if ui != "":
		break
	while f <= round(i/2):
		if i % f == 0 and f != 1:
			f = 1
			break
		elif f == 1:
			1 + 1
		else:
			if round(f + 1) >= round(i/2):
				print(i)
				f = 1
				ui = input("type any key(s) and enter to stop...")
				break
		f += 1
