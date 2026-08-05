a = []
zero_count = 0
for i in range(int(input("Enter the range: "))):
    n = int(input("Enter the number: "))
    if n == 0:
        zero_count += 1
    else:
        a.append(n)
for _ in range(zero_count):
    a.append(0)
print(a)
