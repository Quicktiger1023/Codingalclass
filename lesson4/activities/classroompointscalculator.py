print("Welcome to Classroom Points Calculator")
team1 = int(input("Enter team1 score "))
team2 = int(input("Enter team2 score "))
team3 = int(input("Enter team3 score "))
team4 = int(input("Enter team4 score"))
team5 = int(input("Enter team5 score"))
 
total = team1 + team2 + team3 + team4 + team5
average = total/5
 
print("Total points     :", total)
print("Average per team     :", average)
 
point = 2
stars = total * point
print("Total reward stars :", stars)

boxes = stars // 25
leftover = stars % 25
 
print("Full boxes packed     :", boxes)
print("Leftover stars        :", leftover)

last_week = 500
 
print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)
 
total += 30
print("After bonus points :", total)
 
total -= 15
print("After missed tasks :", total)
 
stars = total * point
boxes = stars // 25
 
print("Final boxes packed :", boxes)