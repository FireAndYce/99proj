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

s = 2
for s in range(2,round((i/2))):
        if (i % s) == 0:
                print("i:" + str(i) + " s:" + str(s))
                result += str(s) + ","
                i = i/s
                s = 2
print(result + str(int(i)))
