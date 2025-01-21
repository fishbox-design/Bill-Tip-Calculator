print("Bill Tip Calculater v2025-01-21")
print("-------------------------------")
bill = float(input("How much is the bill?: "))
person = int(input("How many peoples?: "))
tip_input = int(input("How much is the tip (10, 12 or 15%)?: "))

tip_as_percent = tip_input / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_split = round(total_bill / person, 2)
print("")
print(f"═══════════════════════════════════════════")
print(f"Bill with tip per person is: {bill_split}$ ")
print(f"═══════════════════════════════════════════")
