# Program Title: The ArtBot - Juicebox!
#
# author: Deborah Wang
# date: October 16, 2020
# CMPT 120 -D100
# Week 6 Assignment: Make an Interactive Drawing

###Preliminary Definitons - Imports, Variables, Functions, Design 

##Imports
import turtle
import webbrowser
import random

## Variables
abot = ("Art Bot: ")
colourcodes_site = ('https://www.w3schools.com/colors/colors_names.asp')
colourlist =[]

#Turtle Attributes
bob = turtle.Turtle()
bob.hideturtle()
bob.speed(0)
win = turtle.Screen()
win.setup(450+8,550+4)

#Default colours
default1 = "papayawhip"
default2 = "peachpuff"
default3 = "lightyellow"

##Functions 
#Choose a random colour
def colour_random():
    #This function allows us to randmly choose a colour from a list
    #We remove it from the list to avoid repeats
    colour = random.choice(colourlist)
    colour = colour
    colourlist.remove(colour)
    return colour

##Juice Carton Design
    ##NOTE: the 'change_XX' variable is for another square/star to be create.d
    ##This way, we can create two squares/stars at a specifc coordinate.

def xcor_small_stars(change_s1):
    #Give attributes
    bob.pensize(3)
    bob.color("sandybrown","sandybrown")
    
    #square
    bob.penup()
    bob.setposition(-118+(change_s1*200),148+(change_s1*30))
    bob.pendown()
    bob.begin_fill()
    #creates the square
    for i in range(4):
        bob.forward(6)
        bob.right(90)
    bob.end_fill()

    #lines
    bob.penup()
    bob.goto(-125+(change_s1*200),145+(change_s1*30))
    bob.pendown()
    bob.forward(20)
    bob.penup()
    bob.goto(-115+(change_s1*200),155+(change_s1*30))
    bob.right(90)
    bob.pendown()
    bob.forward(20)
    
    #reset angle
    bob.setheading(0)
    
def ycor_small_stars(change_s2):
    #Give attributes
    bob.pensize(3)
    bob.color("sandybrown","sandybrown")
    
    #square
    bob.penup()
    bob.setposition(-148+(change_s2*260),-142-(change_s2*10))
    bob.pendown()
    bob.begin_fill()
    #creates the square
    for i in range(4):
        bob.forward(6)
        bob.right(90)
    bob.end_fill()

    #lines
    bob.penup()
    bob.goto(-155+(change_s2*260),-145-(change_s2*10))
    bob.pendown()
    bob.forward(20)
    bob.penup()
    bob.goto(-145+(change_s2*260),-135-(change_s2*10))
    bob.right(90)
    bob.pendown()
    bob.forward(20)
    
    #reset angle
    bob.setheading(0)

def xcor_big_stars(change_b1):
    #Give attributes
    bob.pensize(5)
    bob.color("gold","gold")
    
    #square
    bob.penup()
    bob.setposition(-141+(change_b1*260),101+(change_b1*60))
    bob.pendown()
    bob.begin_fill()
    #creates the square
    for i in range(4):
        bob.forward(12)
        bob.right(90)
    bob.end_fill()

    #lines
    bob.penup()
    bob.goto(-155+(change_b1*260),95+(change_b1*60))
    bob.pendown()
    bob.forward(40)
    bob.penup()
    bob.goto(-135+(change_b1*260),115+(change_b1*60))
    bob.right(90)
    bob.pendown()
    bob.forward(40)
    
    #reset angle
    bob.setheading(0)
    
def ycor_big_stars(change_b2):   
    #Give attributes
    bob.pensize(5)
    bob.color("gold","gold")
    
    #square
    bob.penup()
    bob.setposition(-131+(change_b2*240),-180+(change_b2*80))
    bob.pendown()
    bob.begin_fill()
    #creates the square
    for i in range(4):
        bob.forward(12)
        bob.right(90)
    bob.end_fill()

    #lines
    bob.penup()
    bob.goto(-145+(change_b2*240),-185+(change_b2*80))
    bob.pendown()
    bob.forward(40)
    bob.penup()
    bob.goto(-125+(change_b2*240),-165+(change_b2*80))
    bob.right(90)
    bob.pendown()
    bob.forward(40)
    
    #reset angle
    bob.setheading(0)
    

def bottom_carton(change_cb):
    #Give attributes
    bob.color("black")
    bob.fillcolor("white")
    bob.pensize(2)
    bob.penup()
    
    #draw the bottom portion of the carton
    bob.setposition(-96+(change_cb*105),34-(change_cb*10))
    bob.pendown()
    bob.begin_fill()
    bob.right(5-(change_cb*30))
    bob.forward(115-(change_cb*45))
    bob.right(87+(change_cb*30))
    bob.forward(130-(change_cb*10))
    bob.right(93-(change_cb*40))
    bob.forward(115-(change_cb*50))
    bob.right(87+(change_cb*38))
    bob.forward(130)
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)
    
def top_carton1(col_tc1):
    #Give attributes
    bob.color("black")
    bob.fillcolor(col_tc1)
    bob.pensize(2)
    bob.penup()
    bob.setposition(-95,35)
    
    #Draw top carton
    bob.pendown()
    bob.begin_fill()
    bob.right(-45)
    bob.forward(60)
    bob.right(48)
    bob.forward(85)
    bob.right(110)
    bob.forward(50)
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)
    
def top_carton2():
    #Give attributes
    bob.color("black")
    bob.fillcolor("white")
    bob.pensize(2)
    bob.penup()
    bob.setposition(-51,77)
    bob.pendown()
    
    #Draw more details of the top carton
    bob.begin_fill()
    bob.left(90)
    bob.forward(15)
    bob.right(93)
    bob.forward(84)
    bob.right(90)
    bob.forward(15)
    bob.right(90)
    bob.forward(85)
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)
    
def top_carton3(col_tc3):
    #Give attributes
    bob.color("black")
    bob.fillcolor(col_tc3)
    bob.pensize(2)
    bob.penup()
    bob.setposition(33,73)
    bob.pendown()

    #Draw last few details of top carton
    bob.begin_fill()
    bob.right(25)
    bob.forward(43)    
    bob.right(129)
    bob.forward(63)    
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)
    
def label_carton(col_lc):
    #Give attributes
    bob.color("black")
    bob.fillcolor(col_lc)
    bob.pensize(2)
    bob.penup()    
    bob.setposition(-85,15)
    bob.pendown()
    
    #Draw label of carton
    bob.begin_fill()
    bob.right(3)
    bob.forward(80)
    bob.right(87)
    bob.forward(90)
    bob.right(93)
    bob.forward(80)
    bob.right(87)
    bob.forward(90)
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)
    
def fruit_carton(col_fc):
    #Give attributes
    bob.color("black")
    bob.fillcolor(col_fc)
    bob.pensize(2)
    bob.penup()
    bob.setposition(-45,-55)
    bob.pendown()
    
    #draw fruit body    
    bob.begin_fill()
    bob.circle(15)
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)
    
def fruit_carton2():
    #Give attributes
    bob.color("black")
    bob.fillcolor("olivedrab")
    bob.pensize(3)
    bob.penup()
    bob.setposition(-45,-25)
    bob.pendown()
    
    ##draw stems and leaf
    #stem
    bob.begin_fill()
    bob.right(90)
    bob.backward(10)
    bob.forward(10)
    bob.left(45)
    #leaf
    bob.shape("circle")
    bob.shapesize(0.5,0.3,1)
    bob.setposition(-38,-20)
    bob.stamp()
    bob.end_fill()
    
    #reset angle
    bob.setheading(0)

    
#Program begins ...


###Part 1 - Greet User + Get Name

#ask for name
name = str(input("Input your name: ")).capitalize()
nbot = (name+": ")

#welcome
print("\n"+abot+"Welcome "+name+"""!
This program will let you pick some colours and then generate 
a random drawing based on your inputs.
Let's get started!""")


###Part 2 - User Inputs: Colours
print("\nPart 1: Colours")

#Get shape's colour
print(abot+"Get a pen and some paper ready!")
print(abot+"""You will be taken to a website with some colour names.
Please make note of a max of 3 colours (or a min. of 1) you would like to input.

Type in 'yes' when you have read over the instructions.\n""")

ready = str(input(abot+"Ready? ")).lower()
if ready == "yes":
    webbrowser.open(colourcodes_site)

print(("\n"*3)+abot+"Welcome back! How many colours would you like to input?")
stop = int(input(abot+"Number of colors: "))

control = 0
while control !=stop:
    col = str(input(abot+"Colour "+str(control+1)+": ")).lower()
    colourlist.append(col)
    control+=1


###Part 3 - Making the Drawing!
#This part will take the user inputs and define it for the turtle
#Print out a line to let user know that the drawing is being made

##Assign colours to variables
if stop == 1:
    col1 = colour_random()
elif stop ==2:
    col1 = colour_random()
    col2 = colour_random()
elif stop ==3:
    col1 = colour_random()
    col2 = colour_random()
    col3 = colour_random()


print("\n"+abot+"Filling in colours ...\n")

##Execute Drawing


if stop <=2 :
    win.bgcolor(default3)
elif stop ==3:
    win.bgcolor(col3)
print(abot+"Processing drawing ...\n")

#Stars at top of page
xcor_small_stars(1)
xcor_small_stars(0)
xcor_big_stars(0)
xcor_big_stars(1)

#Stars at bottom of page
ycor_small_stars(1)
ycor_small_stars(0)
ycor_big_stars(0)
ycor_big_stars(1)

#Jucie carton outline
bottom_carton(0)
bottom_carton(1)
if stop ==1:
    top_carton1(col1)
    top_carton2()
    top_carton3(default1)
elif stop ==2 or stop ==3:
    top_carton1(col1)
    top_carton2()
    top_carton3(col1)

#Label and fruit
if stop == 1:
    label_carton(col1)
    fruit_carton(default2)
elif stop ==2 or stop ==3:
    label_carton(col1)
    fruit_carton(col2)
fruit_carton2()

###Part 5: Drawing is Generated!
print(abot+"Drawing generated!")

ok = str(input(abot+"Do you see the drawing? ")).lower()
if ok == "yes":
    print(abot+"Awesome! Don't forget to click on the screen to end program.")
    
win.exitonclick()

##END OF PROGRAM
