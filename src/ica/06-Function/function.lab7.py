"""#With 4 turtles, the drawing the boundaries of the petal, then it is filling them in green, then superposing the petals on top of each other, later adding the red inner petal, after it is done with one flower,
it repeats this process n5 times in other locations."""
import turtle
import math
#For green circles
def drawAll:
    def drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, centerX, centerY):
        '''Making a main function using the mini inside functions'''
        for i in range(5):
            drawFiveCircles(sepalTurtle, centerX, centerY)
            drawFiveCircles(petalTurtle, centerX, centerY)
            drawCenterCircle(centerTurtle, centerX, centerY - 15)  # Code for drawing the center
            drawBee(stampTurtle, centerX - 2, centerY)

    def drawFiveCircles(turt, radius, centerX, centerY):
        turt.up()
        turt.goto(centerX, centerY)
        turt.down()

        for i in [0, 1, 2, 3, 4, 5]:  # repeat 5 times
            turt.begin_fill()
            turt.circle(radius)  #
            turt.end_fill()
            turt.left(72)

    def drawCenterCircle(turt, centerX, centerY):
        turt.begin_fill()
        turt.circle(15)
        turt.end_fill()
        for i in [0, 1, 2, 3, 4]  # Repeating 5 times, as we have 5 centers, for each flower
            turt.up()
            turt.goto(centerX, centerY)
            turt.down()

    def drawBee(turt, centerX, centerY):
        turt.stamp()
        for i in [0, 1, 2, 3, 4]
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

    # Reduced code for 1st flower
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)

    # We dont need to define and write sepal and petal everytime now.
    # 2nd turtle

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)

    # 3rd turle
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)

    # 4th turtle
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)

    # 5th flower

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)

    win.exitonclick()


drawAll()
