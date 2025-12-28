print("Welcome to Python Pizze")
bill = 0;
size = input("What size pizza do you want? S, M or L")
if size.lower() == "s":
    bill += 15
elif size.lower() == "m":
    bill += 20
elif size.lower() == "l":
    bill += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni.lower() == 'y':
    if size.lower() == "s":
        bill += 2
    elif size.lower() == 'm' or size.lower() == 'l':
        bill += 3
    
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ")
if extra_cheese.lower() == 'y':
    bill += 1
    
print (f'Your final bill is ${bill}')