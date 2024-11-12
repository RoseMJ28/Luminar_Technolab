y=int(input("Enter the year: "))
if y%100!=0 and y%4==0 or y%400==0:
    print("Leap yr")
else:
    print("Not")
