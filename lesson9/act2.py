print("################################################")
print("welcome to the activity planner")
print("################################################")

# 1. Ask for the holiday type
holiday_type = int(input("select the type of holiday: 1.beach holiday 2.mountain holiday: "))

# 2. Beach Holiday Logic
if holiday_type == 1:
    beach = int(input("select what type of activities u want in beach: 1.swimming 2.sandcastle building: "))
    
    if beach == 1:
        print("u picked:   swimming")
        print("best time:   morning")
        print("remember:    carry sunscreen and water")
    else:
        print("u picked:   sandcastle building")
        print("best time:   evening")
        print("remember:     carry a bucket and a spade")

# 3. Mountain Holiday Logic
elif holiday_type == 2:
    mountain = int(input("select what type of activities u want in the mountain: 1.hiking 2.camping: "))
    
    if mountain == 1:
        print("u picked  : Hiking")
        print("Best for    : Exploring trails")
        print("Remember    : Wear comfortable shoes")
    else:
        print("u picked  : Camping")
        print("Best for    : Staying close to nature")
        print("Remember    : Carry a tent and flashlight")

print("################################################")
print("ur trip has been planned ")
print("enjoy ")
print("################################################")