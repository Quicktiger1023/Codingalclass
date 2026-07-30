print("Welcome to the Weather Outfit Picker")
temp = int(input("enter todays temperature(in degrees celcius)"))

if temp<=20:
    outfit ="jacket"
    print(" u must wear a",outfit)

else:
    outfit ="T-shirt"
    print(" u must wear a",outfit)


rain= input("is it raining or not (yes/no)")
if rain=="yes":
    print("take an umbrella")

else:
    print("dont take an umbrella")


wind= int(input("enter wind speed(in km/h)"))

if wind>=30:
    windSpeedBreaker="yes"
    print("u need a windbreaker")
    
else:
    windSpeedBreaker="no"
    print("thereis no need for a windbreaker")