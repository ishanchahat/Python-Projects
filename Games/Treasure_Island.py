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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
import random

print("Welcome to the Treasure game")

while True:
    direction_choices = ["left", "right"]
    crossing_choices = ["wait", "swim"]
    door_choices = ["red", "yellow", "blue"]

    random.shuffle(direction_choices)
    random.shuffle(crossing_choices)
    random.shuffle(door_choices)

    if door_choices[0] == "blue":
        treasure_location = "blue"
    else:
        treasure_location = "red"

    choice1 = input(f"You're at a crossroad, where do you want to go? Type \"{direction_choices[0]}\" or \"{direction_choices[1]}\": ").lower()
    if choice1 == direction_choices[0]:
        choice2 = input(f"You've come to a lake. There is an island in the middle of the lake. Type \"{crossing_choices[0]}\" to wait for the boat or \"{crossing_choices[1]}\" to swim across: ").lower()
        if choice2 == crossing_choices[0]:
            choice3 = input("You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?: ").lower()
            if choice3 == treasure_location:
                print("You found the Treasure! You win!")
            else:
                print("Sorry, you chose the wrong door. Game Over!")
        else:
            print("You got attacked by an angry shark. Game Over.")
    else:
        print("You fell into a hole. Game Over.")
    
    play_again = input("Do you want to play again? Type y/n: ").lower()
    if play_again != "y":
        break
