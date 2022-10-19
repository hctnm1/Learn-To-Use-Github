
###########
# Imports #
###########

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import simpleplot
import random

#############
# Variables #
#############

# initialize global variables used in your code
secretnr = 0
limit = 0
tries = 0
range = 100

############
# Handlers #
############

# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    global secretnr, limit, tries, range
    secretnr = random.randrange(0, 100)
    limit = 7
    tries = 0
    range = 100
#   print secretnr
    print("New game! Range is from 0 to 100.\nNumber of remaining guesses is " + str(limit) + ".\n")

def range1000():
    # button that changes range to range [0,1000) and restarts
    global secretnr, limit, tries, range
    secretnr = random.randrange(0, 1000)
    limit = 10
    tries = 0
    range = 1000
#   print secretnr
    print("New game! Range is from 0 to 1000.\nNumber of remaining guesses is " + str(limit) + ".\n")

def get_input(guess):
    # main game logic goes here
    global secretnr, limit, tries
    tries += 1
    limit -= 1
    print("Your guess is " + str(guess) + ".")
    if int(guess) == secretnr or limit != 0:
        if int(guess) == secretnr:
            print("Congrats! You guessed the number "+ str(secretnr) + " in " + str(tries) + " tries.\n")
            if range == 100:
                range100()
            elif range == 1000:
                range1000()
        elif int(guess) < secretnr:
            print("Higher!\nRemaining guesses are " + str(limit) + ".\n")
        elif int(guess) > secretnr:
            print("Lower!\nRemaining guesses are " + str(limit) + ".\n")
    else:
        print("You ran out of tries! The number was " + str(secretnr) + ".\n")
        if range == 100:
            range100()
        elif range == 1000:
            range1000()

######
# UI #
######

# create frame
frame = simplegui.create_frame("Guess the number", 100, 150, 100)

# register event handlers for control elements
frame.add_button("Range: 0-100", range100, 100)
frame.add_button("Range: 0-1000", range1000, 100)
frame.add_input("Enter guess:", get_input, 95)

########
# Main #
########

# start frame
frame.start
range100()
