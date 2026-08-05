words = input("Enter the string: ").split()
longest = max(words, key=len) if words else ""
print(longest)
