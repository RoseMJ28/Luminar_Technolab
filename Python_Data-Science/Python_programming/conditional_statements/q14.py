u=int(input("Enter the no of units consumed:"))
if u<=100:
    print("No Charge....")
    u=u-100
else:
 if u<=200:
     u-=100
     rate=u*5
     print("Bill amount is ",rate)
 else:
     u-=200
     rate=(100*5+u*10)
     print("Bill amount is",rate)

