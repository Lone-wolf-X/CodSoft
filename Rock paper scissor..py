import random

def get_user_choice():
    choices = ["rock" , "paper" , "scissor"]
    user_choice = ""
    while user_choice not in choices:
        user_choice = input("\nChoose Rock/Paper/Scissor: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock" , "paper" , "scissor"]
    return random.choice(choices)

def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's Tie"
    elif (user_choice == "rock" and computer_choice == "scissor"):
        return "You win"
    elif (user_choice == "scissor" and computer_choice == "paper"):
        return "You win"
    elif (user_choice == "paper" and computer_choice == "rock"):
        return "You win"
    else:
        return "You lose"
    
def display_result(user_choice , computer_choice, result):
    print(f"\nYou Choose: {user_choice}")
    print(f"Computer choose {computer_choice}")
    print(result)

def Game_play():

    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = winner(user_choice , computer_choice)  

        display_result(user_choice , computer_choice , result)

        if result == "You win":
            user_score += 1
        elif result == "You lose":
            computer_score += 1

        print(f"\nScores:\nYou: {user_score}\nComputer: {computer_score}")

        play_again = input("\n Do you want play again? (yes/no): ").lower()
        if play_again != "yes":
            break

       

Game_play()
print(".........Thanks For Playing :)......")


    
    

