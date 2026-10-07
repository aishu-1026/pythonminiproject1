import random

print("Welcome to Stone Paper Scissors Game")

choices = ["stone", "paper", "scissors"]

while True:
    print("\nChoose one:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "exit" or user_choice == "4":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "stone" and computer_choice == "scissors":
        print("You win!")

    elif user_choice == "paper" and computer_choice == "stone":
        print("You win!")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")

    else:
        print("Computer wins!")
