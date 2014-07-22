###  Pi to the Nth digit
import math

while True:
        try:
                i = int(input("How many digits of pi would you like to see?"))
        except ValueError:
                print("that is not an integer")
                continue
        else:
                break

print(str(math.pi)[0:(i+2)])
