a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("Enter the number3:"))

if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(c,"is largest")
else:
    if b>c:
      print(b,"is largest")
    else:
        print(c,"is largest")