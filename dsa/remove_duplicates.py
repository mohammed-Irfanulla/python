items = input("Enter values separated by space: ").split()
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(" ".join(unique))
