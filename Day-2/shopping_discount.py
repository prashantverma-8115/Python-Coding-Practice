shoammount = int(input("Enter a shopping ammount:"))
if shoammount >= 5000:
    print("20% discount")
elif shoammount>=2000 and shoammount<=4999:
    print("10% discount")
elif shoammount>=1000 and shoammount<=1999:
    print("5% discount")
elif shoammount>=0 and shoammount < 1000:
    print("No discount")
else:
    print("Invalid ammount")  