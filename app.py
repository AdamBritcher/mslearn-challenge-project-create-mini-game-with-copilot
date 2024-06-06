#create a function where a a user can input one of three options "rock", "paper", or "scissors" this should be input into the terminal.  The function will also randomly generate one of the three options.  The function will then determine the winner of the game.  The function will return the result of the game.
def rock_paper_scissors():
    import random
    choices = ['rock', 'paper', 'scissors']
    user_choice = input('Choose rock, paper, or scissors: ')
    while user_choice not in choices:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input('Choose rock, paper, or scissors: ')
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user wins'
    else:
        return 'computer wins'
    
    # print the result: 'tie', 'user wins' or, 'computer wins' to the terminal
    print(f"The user chose {user_choice}, the computer chose {computer_choice}. The result is: {result}")

    #add the option to play another round of the game if the game ends calculate the amount of wins, losses, and ties the user has had and display the results to the terminal.
    user_choice = input('Choose rock, paper, or scissors: ')
    result = rock_paper_scissors(user_choice)
    print(result)
    play_again = input('Do you want to play again? (yes or no): ')
    if play_again == 'yes':
        user_choice = input('Choose rock, paper, or scissors: ')
        result = rock_paper_scissors(user_choice)
        print(result)
    else:
        print('Game over')
        print(f'Wins: {wins}, Losses: {losses}, Ties: {ties}')