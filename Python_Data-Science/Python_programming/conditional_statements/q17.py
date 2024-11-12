yr=int(input("Enter the year: "))
if yr%100==0 and yr%400==0:
    print("CENTUARY")
else:
    print("Not CENTUARY")