n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))
op=input("Enter the operator[+,-,/,*]: ")
if op=='+':
    add = n1  +n2
    print("Sum is ",add)
elif op == '-':
    rem = n1 - n2
    print("Remainder is ", rem)
elif op=='*':
    prod=n1*n2
    print("Product is ",prod)
elif op=='/':
    quo=n1/n2
    print("Quotient is ",quo)
else:
    print("Default Operator")