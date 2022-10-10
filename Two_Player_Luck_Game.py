import random
import turtle

# function to check whether turtle
# is in Screen or not
def isInScreen(win, turt):
	
	# getting the end points of turtle screen
	leftBound = -win.window_width() / 2
	rightBound = win.window_width() / 2
	topBound = win.window_height() / 2
	bottomBound = -win.window_height() / 2

	# getting the current position of the turtle
	turtleX = turt.xcor()
	turtleY = turt.ycor()

	# variable to store whether in screen or not
	stillIn = True

	# condition to check whether in screen or not
	if turtleX > rightBound or turtleX < leftBound:
		stillIn = False
	if turtleY > topBound or turtleY < bottomBound:
		stillIn = False

	# returning the result
	return stillIn


# function to check whether both turtle have
# different position or not
def sameposition(Red, Blue):
	if Red.pos() == Blue.pos():
		return False
	else:
		return True

# main function
def main():

	# screen initialization for turtle
	wn = turtle.Screen()

	# Turtle Red initialization
	# instantiate a new turtle object
	# called 'Red'
	Red = turtle.Turtle()
	
	# set pencolor as red
	Red.pencolor("red")
	
	# set pensize as 5
	Red.pensize(5)
	
	# set turtleshape as turtle
	Red.shape('turtle')
	pos = Red.pos()

	# Turtle Blue initialization
	# instantiate a new turtle object
	# called 'Blue'
	Blue = turtle.Turtle()
	
	# set pencolor as blue
	Blue.pencolor("blue")
	
	# set pensize as 5
	Blue.pensize(5)
	
	# set turtleshape as turtle
	Blue.shape('turtle')
	
	# make the turtle invisible
	Blue.hideturtle()
	
	# don't draw when turtle moves
	Blue.penup()
	
	# move the turtle to a location 50
	# units away from Red
	Blue.goto(pos[0]+50, pos[1])
	
	# make the turtle visible
	Blue.showturtle()
	
	# draw when the turtle moves
	Blue.pendown()

	# variable to store whether turtles
	# are in screen or not
	mT = True
	jT = True

	# loop for the game
	while mT and jT and sameposition(Red, Blue):

		# coin flip for Red
		coinRed = random.randrange(0, 2)

		# angle for Red
		# random.randrange(0, 180)
		angleRed = 90

		# condition for left or right
		# based on coin
		if coinRed == 0:
			Red.left(angleRed)
		else:
			Red.right(angleRed)

		# coin flip for Blue
		coinBlue = random.randrange(0, 2)

		# angle for Blue
		# random.randrange(0, 180)
		angleBlue = 90

		# condition for left or right based
		# on coin
		if coinBlue == 0:
			Blue.left(angleBlue)
		else:
			Blue.right(angleBlue)

		# draw for Red
		Red.forward(50)

		# draw for Blue
		Blue.forward(50)

		# checking whether turtles are in the
		# screen or not
		mT = isInScreen(wn, Blue)
		jT = isInScreen(wn, Red)

	# set pencolor for Blue and Red as black
	Red.pencolor("black")
	Blue.pencolor("black")

	# condition check for draw or win
	if jT == True and mT == False:
		# writing results
		Red.write("Red Won", True, align="center",
				font=("arial", 15, "bold"))
	
	elif mT == True and jT == False:
		
		# writing results
		Blue.write("Blue Won", True, align="center",
				font=("arial", 15, "bold"))
	else:
		# writing results
		Red.write("Draw", True, align="center",
				font=("arial", 15, "bold"))
		Blue.write("Draw", True, align="center",
				font=("arial", 15, "bold"))

	# exit on close
	wn.exitonclick()


# Calling main function
main()
