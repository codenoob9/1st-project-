#Splitwise lite for my flat 
# Electricity 
# Charge per unit
# Grocery
# Per month room charge / Rent
# Extra


rent = int(input("Enter your flat rent = "))
grocery = int(input("Enter the amount of grocery ordered = "))
electricity = int(input("Enter the total of electricity  = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

total_bill = electricity * charge_per_unit

output = (grocery + rent + total_bill) // persons

print("Each person will pay = ", output)