x = int(input("Enter your 1st number: "))
y = int(input("Enter your 2nd number: "))

print("select an operation:")
print("Addition (+)")
print("Subtraction (-)")
print("Multiplication (*)")
print("Division (/)")

op = input("Enter choice (addition, subtraction, multiplication, division, or +, -, *, /):    ")

if op in ("addition","+"):
    a= x+y
    print("result:  ",a)

elif op in ("subtraction","-"):
    b= x-y
    print("result:  ",b)

elif op in ("multiplication","*"):
    c=x*y
    print("result:  ",c)

elif op in ("division", "/"):
    if y==0:
        print("Error: cannnot divide it by zero")
    else:
        d=x/y
        print("result:  ",d)


z=int(input("enter a number"))

print("square (**)")
print("percentage(/100)")

single=input("Enter choice: (square,percentage or **,%)")

if single in ("square","**"):
    e = z*z
    print("result:  ", e)
elif single in ("percentage","%"):
    f = z / 100
    print("result:  ", f)