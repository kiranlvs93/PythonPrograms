"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

while True:
    print("***************************************")
    if input("Welcome to Python Pizza Deliveries! Enter 0 to quit or hit Enter::") == '0':
        break
    size = input("What size pizza do you want? S, M, or L::")
    add_pepperoni = input("Do you want pepperoni? Y or N::")
    extra_cheese = input("Do you want extra cheese? Y or N::")

    bill = 0
    if size.lower() == 's':
        bill += 15
    elif size.lower() == 'm':
        bill += 20
    elif size.lower() == 'l':
        bill += 25
    else:
        print("Allowed sizes for pizza are S/M/L. Please choose again")
        continue

    if add_pepperoni.lower() == 'y':
        if size.lower() == 's':
            bill += 2
        else:
            bill += 3

    if extra_cheese.lower() == 'y':
        bill += 1

    print(f"Your final bill is: ${bill}.")
