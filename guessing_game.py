import statistics
import random
from statistics import mean
from statistics import median
from statistics import mode
high_scores=[]    
thank_you= "Thank you for playing my number guessing game! i hope to see you again" 
not_valid= "That is not a valid entry, please input a number between 1-100"

def welcome():
    print("""
    Welcome to my number guessing game.
    Enter a guess between 1-100
    I will let you know if your number is high or low.
    We score like golf here, Low is good.
    Good luck!
    """)    
       

def end_analytics():
    if len(high_scores)<= 1:
        print("There has been 1 game played.")
    else: 
        print(f"There have been {{}} games played.".format(len(high_scores)))
    
    print(f"The mean of scores is {{}} tries.".format(mean(high_scores)))
    print(f"The median score is {{}} tries.".format(median(high_scores)))
    print(f"The mode of scores is {{}} tries.".format(mode(high_scores)))



def start_game():
    welcome()
    
    solution= random.randint(1,100) 
    guesses=0   

    play_game= input("Would you like to play a number guessing game? Y/N ")

    guess= "" 

    if play_game=="Y": 
        while True:
            try:
                guess= int(input("Please input a guess between 1-100 "))
            except ValueError:
                print(not_valid)
                continue        
            guesses +=1    
            try:  
                if guess <=0:
                    print(not_valid)
                    continue
                if guess >=100:
                    print(not_valid)
                pass     
            except ValueError as err:
                print(not_valid)
                  
            if guess < solution:
                print(f"It's higher")
                continue
            elif guess >solution:
                print(f"It's lower")
                continue   
            else:
                high_scores.append(guesses)
                high_scores.sort()
                print ("Nice Job!")
                print(f"It took you {{}} guesses".format(guesses))
                high_score = f"The current high score is {{}}.".format(min(high_scores))
                print(high_score)
                end_analytics()
                
                play_again=input("would you like to Play again? Y/N ")
                if play_again == "N":
                    print(thank_you)
                    if len(high_scores)>1:
                        end_analytics()
                    break
                if play_again== "Y":
                    print(high_score)
                    solution= random.randint(1,100) 
                    guesses=0         
    else:
        print(thank_you)    
start_game()    
