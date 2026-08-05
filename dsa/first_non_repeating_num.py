s = input("Enter the string: ")
for i, ch in enumerate(s):
    if ch not in s[:i] + s[i+1:]:
        print(ch)
        break
else:
    print("No non-repeating character found")
