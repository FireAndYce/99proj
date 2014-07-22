import math

t = 0
f = 0
l = 1
i = ""


while True:
        try:
                i = int(input("How many iteration(s) would you like to do?"))
        except ValueError:
                print("that is not an integer")
                continue
        else:
                break


for x in range(0,i):
	print(l)
	t = l
	l = l + f
	f = t
	
exit = input("this is the end")

