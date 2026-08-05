a = input("Enter the string: ")
count = sum(1 for ch in a if ch.lower() in "aeiou")
print(count)
