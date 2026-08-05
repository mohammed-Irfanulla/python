import math

a = int(input("Enter the number: "))
if a < 2:
    print("Not prime")
else:
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")
