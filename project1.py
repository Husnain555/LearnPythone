import random

# Dictionary for user choices
dic = {"s": 1, "w": -1, "d": 0}

# Get user input
you = input("Please enter a key between S (Snake), W (Water), D (Gun): ").lower()

if you not in dic:
    print("Sorry, you didn't enter a valid key.")
else:
    user_choice = dic[you]

    computer_choice = random.choice([1, 0, -1])

    choices = {1: "Snake", -1: "Water", 0: "Gun"}
    print(f"You chose {choices[user_choice]}, Computer chose {choices[computer_choice]}.")

    if (user_choice == 1 and computer_choice == -1) or \
       (user_choice == -1 and computer_choice == 0) or \
       (user_choice == 0 and computer_choice == 1):
        print("You Win!")
    elif user_choice == computer_choice:
        print("It's a Tie!")
    else:
        print("Computer Wins!")
