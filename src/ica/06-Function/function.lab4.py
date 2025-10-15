"""#With 4 turtles, the drawing the boundaries of the petal, then it is filling them in green, then superposing the petals on top of each other, later adding the red inner petal, after it is done with one flower,
it repeats this process n5 times in other locations."""
import turtle
import math
#For green circles
def drawFiveCircles (turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()

    for i in [0, 1, 2, 3, 4,5]:  # repeat 5 times
        turt.begin_fill()
        turt.circle(radius) #
        turt.end_fill()
        turt.left(72)

def drawCenterCircle (turt, centerX, centerY):
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()
    for i in [0,1,2,3,4] #Repeating 5 times, as we have 5 centers, for each flower
        turt.up()
        turt.goto(centerX, centerY)
        turt.down()


win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()


petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

#Reduced code for 1st turtle
drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(petalTurtle, 25, 0, 0)
drawCenterCircle(centerTurtle, 0, -15) #Code for drawing the center


stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()


#We dont need to define and write sepal and petal everytime now.
#2nd turtle
drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(petalTurtle, 25, 0, 220)
drawCenterCircle(centerTurtle, 0, 205)

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()


#3rd turle
drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(petalTurtle, 25, 220, 0)
drawCenterCircle(centerTurtle, 220, -15) #Code for drawing the center


stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

#4th turtle
drawFiveCircles(sepalTurtle, 50, 0, -220)
drawFiveCircles(petalTurtle, 25, 0, -220)
drawCenterCircle(centerTurtle, 0, -235)


stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

#5th flower

drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(petalTurtle, 25, -220, 0)
drawCenterCircle(centerTurtle, -220, -235)


stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()

