arr = []
for i in range(6):
    n = int(input(f"Enter element {i}: "))
    arr.append(n)
unique = sorted(set(arr), reverse=True)
if len(unique) >= 2:
    print("Largest:", unique[0])
    print("Second largest:", unique[1])
elif unique:
    print("Only one unique value:", unique[0])
else:
    print("No values entered")
