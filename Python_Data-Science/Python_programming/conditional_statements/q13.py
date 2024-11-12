n=int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print(n,"is a multiple of both 3 and 5")
elif n%3==0:
    print(n,"is a multiple of 3 only")
elif n%5==0:
    print(n,"is a multiple of 5 only")
else:
    print(n,"is not a multiple of 3 and 5")