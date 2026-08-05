import random
import string

lst = []
count = 1
for i in range(10):
    ch = random.randint(1, 2)
    if ch == 1:
        lst.append(random.choice(string.ascii_letters))
    else:
        if count <= 2:
            lst.append(random.choice("#_@$&"))
            count += 1
        else:
            lst.append(random.randint(1, 9))

pwd = "".join(str(item) for item in lst)
print("Your password is:", pwd)
