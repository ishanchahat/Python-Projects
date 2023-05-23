import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock,paper,scissors]

import random
while True:
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))   
    if user_choice not in [0, 1, 2]:
        print("Invalid input. Please enter 0, 1, or 2.")
        continue      
    computer_choice = random.randint(0, 2)  
    print("Your choice:")
    print(game_images[user_choice])
    print("Computer chooses:")
    print(game_images[computer_choice])
    if(user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
        print("You win!")
    elif(user_choice == computer_choice):
        print("Draw!")
    else:
        print("You lose!") 
    play_again = input("Do you want to play again? Type y for yes or n for no: ")
    if play_again.lower() == "n":
        break