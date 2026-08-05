a = input("Enter the numbers separated by spaces: ").split()
rot = int(input("Enter rotation count: "))
rot %= len(a)
result = a[-rot:] + a[:-rot]
print(" ".join(result))
