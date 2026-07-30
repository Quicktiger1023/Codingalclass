field1=int(input("enter the number of crops for field1:      "))
field2=int(input("enter the number of crops for field2:      "))
field3=int(input("enter the number of crops for field3:      "))
field4=int(input("enter the number of crops for field4:      "))
field5=int(input("enter the number of crops for field5:      "))

total= field1+field2+field3+field4+field5
avg= total/5

print("the total number of crops is equal",total)
print("the average number of crops is equal to",avg)

pp_kg=20
earnings= total*pp_kg
print("the total earnings is Rs",earnings)

bags=total//20
remaining=total%20
print("total there are"+ bags +"bags")
print("the remaining amount of bags is ",remaining)

last=300
print("better than last year? :", total>last)
print(" same as last year :", total==last)
print("at least as good as last year? :", total>=last)

total+= 50
print("After bonus the total crop is", total)

total-= 10
print("total after removing seed:",total)

bags = total//20
print("finally bags needed are:",bags)