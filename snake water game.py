import random

def play_game():
    print("--- Welcome to the Snake, Water, Gun Game! ---")
    print("Rules: Snake drinks Water (Snake wins), Water douses Gun (Water wins), Gun shoots Snake (Gun wins).\n")
    
    # Mapping numbers to game choices
    choices = {1: "Snake", 2: "Water", 3: "Gun"}
    
    # Get user choice with input validation
    print("Choose your option:")
    print("1: Snake")
    print("2: Water")
    print("3: Gun")
    
    try:
        user_choice_num = int(input("Enter your choice (1, 2, or 3): "))
        if user_choice_num not in:
            print("Invalid input! Please run the game again and choose 1, 2, or 3.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number (1, 2, or 3).")
        return

    # Computer choice using random.randint
    comp_choice_num = random.randint(1, 3)
    
    user_choice = choices[user_choice_num]
    comp_choice = choices[comp_choice_num]
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {comp_choice}\n")
    
    # Game Logic to determine the winner
    if user_choice_num == comp_choice_num:
        print("It's a Tie! Both chose the same.")
    elif (user_choice_num == 1 and comp_choice_num == 2) or \
         (user_choice_num == 2 and comp_choice_num == 3) or \
         (user_choice_num == 3 and comp_choice_num == 1):
        print(f" You Win! {user_choice} beats {comp_choice}.")
    else:
        print(f" Computer Wins! {comp_choice} beats {user_choice}.")

# Run the game
if __name__ == "__main__":
    play_game()
