#Solo project, creating a sophisticated Turtle graphic:

#I want to create a picture of a Minion. From despicable me

#Drawing a yellow oval
import turtle
import math


def drawoval(turt, angle, longradius, shortradius, centerX, centerY): #So the turtle is oval
  turt.left(angle)
  turt.penup()
  turt.goto(centerX, centerY)
  turt.pendown()
  turt.hideturtle()

  for i in range(2):

    turt.begin_fill()
    turt.circle(longradius, 90)
    turt.circle(shortradius, 90)
    turt.end_fill()


def drawrectangle(turt, angle, length, width, centerX,centerY):
    turt.left(angle)
    turt.penup()
    turt.goto(centerX, centerY)
    turt.pendown()
    turt.hideturtle()

    for i in range(2):
        turt.begin_fill()
        turt.forward(length)
        turt.left(90)
        turt.forward(width)
        turt.left(90)
        turt.end_fill()

def draw_bottom_half_oval(turt, angle, longradius, shortradius, centerX, centerY):
    turt.left(angle)
    turt.penup()
    turt.goto(centerX, centerY)
    turt.pendown()
    turt.hideturtle()

    turt.begin_fill()
    turt.circle(-longradius, 90)   # negative radius → clockwise
    turt.circle(-shortradius, 90)
    turt.end_fill()

def drawcircle(turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.hideturtle()
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()

def drawcircleboundary(turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.hideturtle()
    turt.circle(radius)

def draw_arc(turt, angle,radius, centerX,centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.hideturtle()
    turt.circle(radius,angle)

def drawhair(turt,angle, centerX,centerY):
    turt.left(angle)
    turt.penup()
    turt.goto(centerX, centerY)
    turt.pendown()

    for i in range(20):
        turt.forward(1)
        turt.left(2)  # gradual turn → smooth curve


#  BACKGROUND CHOICE


def draw_sun(turt):
    turt.penup()
    turt.goto(300, 250)
    turt.pendown()
    turt.color("gold")
    turt.begin_fill()
    turt.circle(80)
    turt.end_fill()

    num_rays = 12  # number of rays
    ray_length = 40  # length of each ray

    for i in range(num_rays):
        angle = 360 / num_rays * i
        turt.penup()
        # Calculate position at sun edge
        x = 300 + 80 * math.cos(math.radians(angle))
        y = 330 + 80 * math.sin(math.radians(angle))
        turt.goto(x, y)
        turt.setheading(angle)
        turt.pendown()
        turt.forward(ray_length)



def draw_moon(turt):
    turt.penup()
    turt.goto(300, 250)
    turt.pendown()
    turt.color("lightgrey")
    turt.begin_fill()
    turt.circle(80)
    turt.end_fill()

    #Making crescent:
    turt.penup()
    turt.goto(350, 250)
    turt.pendown()
    turt.color("royal blue")
    turt.begin_fill()
    turt.circle(80)
    turt.end_fill()




win = turtle.Screen()
#Asking the user what time or day they want.

time_of_day = win.textinput("Minion Time", "What time of the day is it for the minion? (day or night): ")


# Adjusting backg orund to the time they want
sky = turtle.Turtle()
sky.hideturtle()
sky.speed(0)

if time_of_day and time_of_day.lower() == "day":
    win.bgcolor("light yellow")
    draw_sun(sky)
else:
    win.bgcolor("royal blue")
    draw_moon(sky)


#Drawing the body
body = turtle.Turtle()
body.speed(0)
body.color("yellow")


#I need two yellow small arms
#At the position, center + forward(radius) draw one arm and another arm at
arms = turtle.Turtle()
arms.speed(0)
arms.color("yellow")

hands = turtle.Turtle()
hands.speed(0)
hands.color("black")

legs = turtle.Turtle()
legs.speed(0)
legs.color("dark blue")

feet = turtle.Turtle()
feet.speed(0)
feet.color("grey")

suit = turtle.Turtle()
suit.speed(0)
suit.color("dark blue")

eyes = turtle.Turtle()
eyes.speed(0)
eyes.color("white")

pupil = turtle.Turtle()
pupil.speed(0)
pupil.color("burlywood")

iris = turtle.Turtle()
iris.speed(0)
iris.color("black")

glasses = turtle.Turtle()
glasses.speed(0)
glasses.pensize(6)
glasses.color("light grey")

smile= turtle.Turtle()
smile.speed(0)
smile.pensize(2)
smile.color("black")
#
drawoval(body,45, 100, 50, 0, 0)
#I need one small arms at the right
drawoval(arms, 70,50, 0.2, 50, 0)
#I need one small hand at the right
drawoval(hands, 180,20, 2, 50, 0)
#I need one small arms at the left
drawoval(arms, -70,50, 0.2, -120, 0)
#I need one arm at the left
drawoval(hands, 90,20, 2, -120, 0)
#I need two long blue legs
drawrectangle(legs, 90, 60, 20, -5,-70)

drawrectangle(legs, 0, 60, 20, -40,-70)

drawrectangle(feet, 0, 30, 10, -25, -80)
drawrectangle(feet, 0, 30, 10, -60, -80)

#Drawing the minion suit:
draw_bottom_half_oval(suit, -125, 68, 10, 20, 10)

#Draw eyes:
drawcircle(eyes, 25, -35, 60)
drawcircle(pupil, 10, -35, 75)
drawcircle(iris, 5, -35, 80)

#Drawing glasses:
drawcircleboundary(glasses,25,-35,60)
drawrectangle(glasses, 20, 38, 2, -6, 85)
drawrectangle(glasses, 140, 38, 2, -60, 85)



#Drawig the smile:
draw_arc(smile, 30,80,-50,20)

#Draw hair
drawhair(smile,80, -40,150)
drawhair(smile,-100, -40,150)
drawhair(smile,0, -40,150)
win.exitonclick()