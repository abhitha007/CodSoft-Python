import random
import pickle


PROFILES_FILE = 'user_profiles.pkl'

def load_profiles():
    """Load user profiles from the file."""
    try:
        with open(PROFILES_FILE, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_profiles(profiles):
    """Save user profiles to the file."""
    with open(PROFILES_FILE, 'wb') as file:
        pickle.dump(profiles, file)

def get_computer_choice(difficulty):
    """Generate computer choice based on difficulty level."""
    choices = ["rock", "paper", "scissors"]
    if difficulty == "easy":
        return random.choice(choices)
    elif difficulty == "medium":
        
        last_choice = get_last_user_choice()
        if last_choice:
            return {
                "rock": "paper",
                "paper": "scissors",
                "scissors": "rock"
            }.get(last_choice, random.choice(choices))
    return random.choice(choices)

def get_last_user_choice():
    """Retrieve the last user choice from the profile."""
    profiles = load_profiles()
    if profiles:
        for profile in profiles.values():
            return profile.get('last_choice')
    return None

def update_last_user_choice(user, choice):
    """Update the last user choice in the profile."""
    profiles = load_profiles()
    if user not in profiles:
        profiles[user] = {}
    profiles[user]['last_choice'] = choice
    save_profiles(profiles)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def print_result(user_choice, computer_choice, result):
    """Print the result of the game."""
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    profiles = load_profiles()
    
    user = input("Enter your name: ")
    if user not in profiles:
        profiles[user] = {'wins': 0, 'losses': 0, 'ties': 0}
    
    while True:
        difficulty = input("\nChoose difficulty level (easy/medium): ").lower()
        if difficulty not in ["easy", "medium"]:
            print("Invalid difficulty level. Please choose easy or medium.")
            continue
        
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice(difficulty)
        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)
        
        if result == "win":
            profiles[user]['wins'] += 1
        elif result == "lose":
            profiles[user]['losses'] += 1
        else:
            profiles[user]['ties'] += 1
        
        update_last_user_choice(user, user_choice)
        save_profiles(profiles)
        
        print(f"Score - Wins: {profiles[user]['wins']} | Losses: {profiles[user]['losses']} | Ties: {profiles[user]['ties']}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
