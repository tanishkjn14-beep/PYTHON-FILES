name = input("Enter your real name, Agent: ")
gadget = input("Enter your favourite gadget: ")

agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

print("Name:", name, "-> type:", type(name))
print("Gadget:", gadget, "-> type:", type(gadget))
print("agent number:", agent_number, "-> type:", type(agent_number))
print("speed rating:", speed_rating, "-> type:", type(speed_rating))
print("mission count:", mission_count, "-> type:", type(mission_count))
print("Is active:", is_active, "-> type:", type(is_active))

agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("agent number as text:", agent_number_text, "-> type:", type(agent_number_text))
print("mission count as text:", mission_count_text, "-> type:", type(mission_count_text))
print("speed rating as text:", speed_rating_text, "-> type:", type(speed_rating_text))
print("status as text:", status_text, "-> type:", type(status_text))

first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("first 3 letters of name:", first_three)
print("last letter of name:", last_letter)
print("secret code name:", code_name)

reversed_gadget = gadget[::-1]