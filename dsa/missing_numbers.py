lst = []
for i in range(int(input("Enter the size: "))):
    n = int(input("Enter number: "))
    lst.append(n)
if lst:
    start = min(lst)
    end = max(lst)
    missing = [str(i) for i in range(start, end + 1) if i not in lst]
    print("Missing numbers:", " ".join(missing))
else:
    print("No numbers entered")
