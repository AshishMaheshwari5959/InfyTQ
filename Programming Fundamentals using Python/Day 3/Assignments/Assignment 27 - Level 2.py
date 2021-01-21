import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle

#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern

alex.color("green")
for i in range(1,5):
    alex.circle(60-10*i)
    
alex.right(120)
alex.color("blue")
for i in range(1,5):
    alex.circle(60-10*i)

alex.right(120)
alex.color("red")
for i in range(1,5):
    alex.circle(60-10*i)
