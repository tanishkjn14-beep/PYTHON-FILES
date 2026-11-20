print("PERSONAL GOALS DISPLAY")

import keyword

person_name= input("Enter your name: ")
goal_name= input("Enter one skill you want to get better at: ")
target_month= input("Enter the month you want to reach it by: ")

daily_minutes= 30

print(person_name, "plans to work on", goal_name, "for", daily_minutes, "minutes every day until", target_month)

print("\nwords python has reserved for itself:\n")
print(keyword.kwlist)