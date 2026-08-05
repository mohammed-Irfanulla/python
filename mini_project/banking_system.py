amt = 5000

def deposit(x):
    global amt
    amt += abs(x)
    print("available amt:", amt)


def withdraw(x):
    global amt
    if (amt - x) < 300:
        print("minimum bal amt to be 300!")
    else:
        amt -= x
        print("available amt:", amt)


if __name__ == "__main__":
    n = 'y'
    while n == 'y':
        ch = int(input("1.deposit 2.withdraw 3.balance: "))
        if ch == 1:
            deposit(int(input("enter amt: ")))
        elif ch == 2:
            withdraw(int(input("enter amt: ")))
        elif ch == 3:
            print(amt)
        else:
            print("invalid input")
        n = input("do you want to continue? y/n: ").lower()
