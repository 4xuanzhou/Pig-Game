import random
     
def print_instructions():
    '''
    This function tells the users the rules of the game.
    '''
    print("Game starts")
    print("You and the computer take turns to roll a six-sided dice.",
    "On each turn, you roll the dice as many times as you wish, or until you roll a 6.",
    "Each number you roll, except a 6, is added to your score this turn.",
    "But if you roll a 6, your score for this turn is zero, and your turn ends.",
    "At the end of each turn, the score for that turn is added to your total score.",
    "The first player to reach or exceed 50 wins.",
    "The computer always goes first, so you get one more turn if the computer is the first to reach 50.",
    "If both players are tied with 50 or more, each gets another turn until the tie is broken.")
    print("="*80)
    

def computer_move(computer_score, human_score):
    '''
    This function displays the result of each roll, and returns the result (either 0 or the total of the rolls).
    '''
    result = 0
    
#When the computer is ahead or there is a tie, it rolls two times each turn.    
    if computer_score >= human_score:
        for i in range(2):
            x = roll()
            print(x)
            if x == 6:
                result = 0
                break
            result += x
            
#When the computer is behind, it rolls four times each turn.    
    if computer_score < human_score:
        for i in range(4):
            x = roll()
            print(x)       
            if x == 6:
                result = 0
                break        
            result += x
     
    return result
    print("Computer got", result, "this turn.")
        

def human_move():
    '''
    This function repeatedly asks whether the user wants to roll again and displays the result of each roll.
    '''
    print("-"*80)
    print("Your turn!")

#Ask the player to enter 'Y' to start rolling the dice.
#If the player enters other characters, the prompt appears again.    
    first_roll = ask_first_roll("Enter 'Y' to roll the dice!")
    if first_roll == True:
        result = roll()
        
    print(result)
    
    if result != 6:
        while 1==1:
            roll_again = ask_yes_or_no("Roll again? Please enter 'Y' or 'N'.")
            if roll_again == True:
                x = roll()
                if x != 6:         
                    print(x)
                    result += x
                else:
                    print(x)
                    result = 0
                    break
            else:
                break

    else:
        result = 0
                
    return result
    print("You got", result, "this turn.")    

   
def is_game_over(computer_score, human_score):
    '''
    This function returns True if either player has 50 or more, and the players are not tied, otherwise it returns False.
    '''
    print("Is the game over?")
    if computer_score!=human_score and computer_score>=50:
        return True
        
    elif computer_score!=human_score and human_score>=50:
        return True
        
    else:
        return False


def roll():
    '''
    This function returns a random number in the range 1 to 6.
    '''  
    num = random.randint(1, 6)
    return num

def ask_first_roll(prompt):
    '''
    This function prints the prompt as a question to the user to start the first roll.
    '''
    while 1 == 1:
        start = input(prompt)

        if start[0] == 'Y' or start[0] == 'y':
            return True
            break

def ask_yes_or_no(prompt):
    '''
    This function prints the prompt as a question to the user whether they want to roll again or play again.
    '''
    while 1 == 1:
        again = input(prompt)
       
        if again[0] == 'N' or again[0] == 'n':  
            return False
            break

        if again[0] == 'Y' or again[0] == 'y':
            return True
            break


def show_current_status(computer_score, human_score):
    '''
    This function prints the user’s current score and the computer's current score, how far behind (or ahead) the user is, or if there is a tie.
    '''   
    print("Your current score is "+ str(human_score) + ".")
    print("Computer's current score is " + str(computer_score) + ".")
    if computer_score>human_score:
        print("You are", str(computer_score-human_score), "behind.")
    elif computer_score<human_score:
        print("You are", str(human_score-computer_score), "ahead.")
    else:
        print("There is a tie.")
    

def show_final_results(computer_score, human_score):
    '''
    This function tells whether the human won or lost, and by how much.
    '''
    if computer_score>human_score:
        print("You lost by " + str(computer_score-human_score) + ".")
    elif computer_score<human_score:
        print("You won by " + str(human_score-computer_score) + ".")




def main():
    '''
    This is where your program will start execution.
    '''        
    while 1 == 1:
        print_instructions()
        
        computer_score = 0
        human_score = 0
        while 1==1:
            print("Computer's turn:")
#Call the computer move.            
            computer_score += computer_move(computer_score, human_score)
            
            show_current_status(computer_score, human_score)
#Call the human move.            
            human_score += human_move()
            
            show_current_status(computer_score, human_score)

            game_over = is_game_over(computer_score, human_score)
            if game_over == True:
                print(game_over)
                break
#If the game is not yet over, print "False" and start one more round.
            else:
                print(game_over)
                print("-"*80)
                    

        show_final_results(computer_score, human_score)
        print("="*80)


        play_again = ask_yes_or_no("Do you want to play again? Please enter 'Y' or 'N'.")
        if play_again == False:
            print("Bye!")
            break
        else:
            print("="*80)

    
    
if __name__ == "__main__":
    main()


