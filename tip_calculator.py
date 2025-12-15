print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
split = int(input ("How many people to split the bill?\n"))
tip = (tip / 100) * bill
total = (tip + bill) / split
print(f"Each person should pay: ${round(total, 2)}")