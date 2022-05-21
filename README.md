#A Number Guessing Game

Team Treehouse Python Techdegree Project 1: A Number Guessing Game

##Project Requirements
"""Psuedo-code Hints
    
    #When the program starts, we want to:
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.
    
    ( You can add more features/enhancements if you'd like to. )
    
     write your code inside this function.
Kick off the program by calling the start_game function.

### Exceeds expectations requirements

    1. As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
    2. as a player of the game, after I guess correctly I should be prompted if I would like to play again.
    3. As a player of the game, at the start of each game I should be shown the current high score (least amount of points), so that I know what I am supposed to beat.

## My Methodology

I read the psuedo-code hints and the first thing i did was create the known variables, funtions, and list(s) that thought i would need.
I worked line by line to to build each individual part of the code.
  - I built my funtions in a counter-intuitive way in the fact that i built sections that would repeat themselves then after i knew they worked i would go and build the fuction. This allowed me to make sure everything was doing what i was intending it too.
  -   A great example of this was the end_analytics fuction that i used. I tried creating one in the beginning but couldnt get the behavior that i wanted out of the function so i built it as copy pasta fisrt, then replaced it after.
  -   My goal was to go for "Exceeds expectations" with this project, so i made sure to include those in my "must haves" when planning out how i was going to make this code.
I definitely wanted to build additional features when i saw it was allowed the two additional features i wanted.
  -   The high score to also displat the name of the person that got it.
  -   There to be a difficulty level
       - The difficulty was something that I thought of very late in the process.
       - It ended up being much easier than i expected, but it was a good example of "someone will always want changes to your code", and in this case i was the "someone".