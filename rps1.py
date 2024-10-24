import random
def get_computer_choice():
    return random.choice(["rock","paper","scissor"])
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "scissor" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"
def play_game():
    user_score, computer_score =0,0

    print("Welcome to ROCK, PAPER, SCISSOR!")
    while True:
        user_choice = input("choose rock, paper or scissor: ")
        if user_choice not in ["rock","paper","scissor"]:
            print("invalid choice! please choose rock, paper or scissor")
            continue
        computer_choice = get_computer_choice()
        print("\nYou chose:", user_choice)
        print("computer chose:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("it's a tie")
        elif result == "user":
            print("you win!")
            user_score += 1
        else:
            print("computer win!")
            computer_score +=1
        
        print("Scores: You:", user_score, "computer:", computer_score)

        play_again = input("Do you want to play again? (yes/No): ")
        if play_again != "yes":
            print("Thanks for playing!, the scores:")
            print("You:", user_score, "computer:", computer_score)
            break
if __name__ == "__main__":
    play_game()