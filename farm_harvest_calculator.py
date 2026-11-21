field1 = input("field1 harvest in kg ")
field2 = input("field2 harvest in kg ")
field3 = input("field3 harvest in kg ")
field4 = input("field4 harvest in kg ")
field5 = input("field5 harvest in kg ")

total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("total harvest    :", total, "kg")
print("average per field  :", average, "kg")

price_per_kg = 15
earnings = total * price_per_kg
print("total earnings   : rs.", earnings)

bags = total // 25
leftover = total % 25

print("Full bags packed :", bags)
print("leftover grain  :", leftover, "kg")

last_year = 500
print("better than last year?  :", total > last_year)
print("same as last year?      :", total == last_year)
print("at least as good?       :", total >= last_year)

total += 30
print("after bonus crop   :", total, "kg")

total -= 15
print("after seed reserve :", total, "kg")

bags = total // 25
print("final bags packed :", bags)

print("total harvest: ",total) 