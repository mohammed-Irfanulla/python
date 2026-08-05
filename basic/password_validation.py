pwd = input("Enter the password: ")
lwcase = 0
upcase = 0
spc = 0
dig = 0
if len(pwd) >= 8:
    for i in pwd:
        if i.isdigit():
            dig += 1
        elif i.isalpha():
            if i.islower():
                lwcase += 1
            if i.isupper():
                upcase += 1
        else:
            spc += 1
    if lwcase > 1 and upcase > 1 and spc >= 1:
        print("Strong password!")
    else:
        print("Weak password!")
else:
    print("Password too short")
