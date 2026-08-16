n= int(input("enter the number of rows in the rows:     "))

for i in range(n):#it means for will here go from 0 to n-1
    for j in range(i): # if n=5,then for will go from 0 to 4
        #i and j here are just an iterater which keeps changing its value according to range
        print("#", end=" ")
    print(  )