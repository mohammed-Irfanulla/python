a = input("Enter first string: ")
b = input("Enter second string: ")
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not anagram")
