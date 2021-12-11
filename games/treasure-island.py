print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
Follow the instructions and make your choices to reach the treasure
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
if input("Which side do you want to go? LEFT or RIGHT?").lower() == "left":
    print("You fell into a hole. GAME OVER. Try again")
elif input("Do you want to SWIM or WAIT?") == "swim":
    print("You are feast for crocodiles in the water. GAME OVER. Try again")
elif door := input(
        "Good you waited. You've arrived at the castle in the boat. Which door do you want to open. RED,BLUE,YELLOW?"):
    if door.lower() == "red":
        print("You got roasted in fire. GAME OVER. Try again")
    elif door.lower() == "blue":
        print("You got poisoned. GAME OVER. Try again")
    else:
        print("YAAAY!! You found the treasure. Congratulations!!!")
