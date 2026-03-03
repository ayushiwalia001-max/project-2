import random

def get_choice():
    player_choice = input("Enter you choice(rock/paper/scissors):").lower()
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)
    choices  = {"player":player_choice,"computer":computer_choice}
    return choices

def  check_win(player,computer):
    print(f"player choose {player}, computer choose {computer}")
    if player == computer:
        return "it's a tie!"
    elif player =='rock':
        if computer =="scissors":
            return "rock smashes scissors! you win!"
        else:
            return "paper covers rock! computer wins!"
    elif player =='paper':
        if computer == 'rock':
            return "paper covers  rock! you win!"
        else:
            return 'scissors cut paper! computer wins!'
    elif player =='scissors':
        if computer == 'paper':
            return "scissors cut paper! you win!"
        else:
            return "rock smashes scissoers! computer wins!"       

        
        
choice  = get_choice()
result = check_win(choice['player'],choice['computer'])
print(result)