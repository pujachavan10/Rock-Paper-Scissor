import random 
# Import the random module for the computer's random choice

emojis = {'r':'🪨', 'p': '📰', 's':'✂️'}  
# Dictionary mapping for user-friendly emoji representation
choices = ('r','p','s')  
# Valid options for the game (rock, paper, scissors)

# Main game loop
while True:
    # Get the user's input and convert it to lowercase
    user_choice = input('Rock, paper or scissor? (r/p/s): ').lower()
    # Validating the user input and prompt again for invalid input
    if user_choice not in choices:
        print('Invalid Input')
        continue

    # Randomly choose value for the computer
    computer_choice = random.choice(choices)

    # Display the choices of the user and computer using emojis
    print(f'Your choice: {emojis[user_choice]}')
    print(f'Computer choice: {emojis[computer_choice]}')

    # Determine the outcome of the game
    if user_choice == computer_choice:
        print('It\'s a tie!!')  # When both choices are the same
    elif (
        (user_choice == 'r' and computer_choice == 's') or  # Rock beats scissors
        (user_choice == 's' and computer_choice == 'p') or  # Scissors beats paper
        (user_choice == 'p' and computer_choice == 'r')     # Paper beats rock
    ):
        print('You win')  # User wins with the above conditions
    else:
        print('haha sucker, I win')  # Computer wins otherwise

    # Ask the user whether they want to continue playing
    idk = input('Continue (y/n)? ').lower()
    if idk == 'n':  # Exit the loop if the user chooses 'n'
        break  # End the program
