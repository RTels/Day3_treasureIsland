print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to the Treasure Island. Your mission is to find the treasure.")
path_1 = input('You\'re at a cross road. Where do you want to go?\n    Type "left" or "right"\n').lower()

if path_1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.\n")
    path_2 = input("    Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if path_2 == "wait":
        path_3 = input("You arrived at the island unharmed. There are three doors: one red, one yellow and one blue. "
              "Which colour do you choose?\n").lower()
        if path_3 == "red":
            print("It's a room full of fire. You are burned to death. Game over!")
        elif path_3 == "yellow":
            print("You found the treasure. You win!")
        elif path_3 == "blue":
            print("You enter a room full of humanoid beasts. Game over!")
        else:
            print("You choose a door that doesn't exist. A fiend spawns behind you and eats you alive. Game over")

    else:
        print("You got attacked by a giant trout and died. Game over!")

else:
    print("You fell into a hole. Game over!")


