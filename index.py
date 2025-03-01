import random

choices = ["rock","paper","sissors"]

player_choice = input("Enter your choice:").lower()
 
computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print(f"dono ka choice same hai {player_choice} tha. Its a tie!")
elif player_choice == "rock" and computer_choice == "sissors":
    print(f"Player wins! {player_choice} beats {computer_choice}.")


elif player_choice == "paper" and computer_choice == "rock":
    print(f"Players wins! {player_choice} beats {computer_choice}.")

elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Players wins! {player_choice} beats {computer_choice}.")

else:
    print(f"Computer wins! {computer_choice} baets {player_choice}. ")
    


