import random

# Picks a number from 1 to 100, sets number of attempts to 1, and the guessed number to 0 (to )
num_random = random.randint(1, 100)
num_attempts = 1
num_guess = 0
like_to_play = True

#sets up a loop to keep playing until user is done.
while(like_to_play == True) :
    #runs a loop as long as the guessed number isn't the same as the random number
    while(num_guess != num_random) :
        if num_guess == 0 :
            #prompts the user to pick a number between 1 and 100 only on the first guess
            num_guess = int(input("I'm thinking of a number between 1 and 100. Try and guess it if you dare >:)\n"))
        #check if the guessed humber is higher, if so, print "Guess Lower"
        if num_guess > num_random :
            num_guess = int(input("Try again. Guess lower this time. \n"))
            num_attempts += 1
        #check if the guessed humber is higher, if so, print "Guess Higher"
        elif num_guess < num_random :
            num_guess = int(input("Try again. Guess higher this time. \n"))
            num_attempts += 1
        else :
            continue
        
    print("You got it", end="")
    if num_attempts == 1 :
        print("! First try?? You must be cheating!\n")
    elif num_attempts >= 10 :
        print("... Wow, more than 9 tries? You suck at this game.\n")
    elif num_attempts >= 8 and num_attempts <=9 :
        print(". Well, I guess you got it eventually...after 8 or 9 tries...\n")
    elif num_attempts >= 6 and num_attempts <=7 :
        print("! Nice! You took 6 or 7 tries. (Insert unkown meme here)")
    elif num_attempts >= 4 and num_attempts <=5 :
        print("! Good job! You got it in 4 or 5 tries.")
    else :
        print("! Impressive!")
    num_guess = 0 
    play_again = input("Do you want to Play again? Y or N\n")
    if play_again.upper() == "N" :
        like_to_play == False

