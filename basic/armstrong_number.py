a = input("Enter the number: ")
count = len(a)
total = sum(int(n) ** count for n in a)
if total == int(a):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
