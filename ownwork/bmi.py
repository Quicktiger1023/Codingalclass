weight= int(input("enter ur weight:     "))
height= int(input("enter ur height:     "))

bmi= weight/(height**2)

if bmi<=18.5:
    print("you are underweight as ur bmi is",bmi)
elif bmi<=25:
    print("you have a normal weight as ur bmi is",bmi)
elif bmi<=30:
    print("you are overweight as ur bmi is ",bmi)
else:
    print("you are obese as ur bmi is",bmi)