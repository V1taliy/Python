print("Welcome to the tip calculator!")
bill = float(input("Enter the total bill? $"))
tip = int(input("Enter how much tip would you like to give? 10, 15, 20? "))
people = int(input("Enter how many people should split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")