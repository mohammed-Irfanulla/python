s = input("Enter sentence: ").lower().split()
vowels = []
consonants = []
for word in s:
    for ch in word:
        if ch.isalpha():
            if ch in "aeiou":
                vowels.append(ch)
            else:
                consonants.append(ch)
print("Vowels:", vowels)
print("Consonants:", consonants)
