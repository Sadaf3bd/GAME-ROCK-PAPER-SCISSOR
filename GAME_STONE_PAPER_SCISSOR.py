import random

def play_game():
    print("Welcome to Rock, Paper & Scissor 🎮👾")
    name = input("Enter Username: ")
    option = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter quit to exit the game OR \n Choose Rock, Paper, Scissor: ").lower()

        # USER CHOSE

        if user_choice == "quit":
            print(f"Thanks for playing {name} , BYE 👋")
            break
        if user_choice not in option:
            print("Invalid choice! Please try again.")
            continue

        # BOT CHOSE
        
        bot_choice = random.choice(option)
        print(f"Bot Chose: {bot_choice}")

        # DECIDE WINNER

        if user_choice == bot_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and bot_choice == "scissor") or \
                (user_choice == "paper" and bot_choice == "rock") or \
                (user_choice == "scissor" and bot_choice == "paper"):
            print(f"{name} ❕ You Win 🏅🎉")

        else:
            print(f"You Lost {name} 🤕 ")

        # PLAY AGAIN OPTION

        play_again = input("Do you want to play again? Enter Yes or No: ").lower()
        if play_again not in ["yes"]:
            print(f"Thanks for playing {name} , BYE 👋")
            break

play_game()





