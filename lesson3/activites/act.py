
name = input("Enter your real name, Club Member: ")
club = input("Enter your school club name: ")
 

member_number = int(input("enter ur number:-    "))
points_earned = int(input("enter ur points which u earned:-    "))
event_count = int(input("enter ur event count:-    "))
meeting_hours = int(input("enter ur meeting hours:-    "))
is_active = True
 

print("Name:", name, "-> type:", type(name))
print("Club:", club, "-> type:", type(club))
print("Member Number:", member_number, "-> type:", type(member_number))
print("Points Earned:", points_earned, "-> type:", type(points_earned))
print("Event Count:", event_count, "-> type:", type(event_count))
print("Meeting Hours:", meeting_hours, "-> type:", type(meeting_hours))
print("Is Active:", is_active, "-> type:", type(is_active))
 

member_number_text = str(member_number)
event_count_text = str(event_count)
points_text = str(points_earned)
status_text = str(is_active)
 
print("Member Number as text:", member_number_text, "-> type:", type(member_number_text))
print("Event Count as text:", event_count_text, "-> type:", type(event_count_text))
print("Points as text:", points_text, "-> type:", type(points_text))
print("Status as text:", status_text, "-> type:", type(status_text))
 

first_three = name
last_letter = name
badge_code = first_three + last_letter
 
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Badge Code:", badge_code)
 

reversed_club = club
print("Reversed Club Name:", reversed_club)
 

badge_line_1 = "CLUB MEMBER " + badge_code
badge_line_2 = "ID: " + member_number_text + " | EVENTS: " + event_count_text
badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = "SECRET CLUB CODE: " + reversed_club
 

print("##############################################################")
print("                 SCHOOL CLUB MEMBER BADGE                        ")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("##############################################################")
