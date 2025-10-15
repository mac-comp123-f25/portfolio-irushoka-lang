import turtle

def draw_nested_squares(turtle):
    for side_length in range(10, 80, 10): #Outerloop #You can also just aassign a value a range, don't need to define it
        for i in range(4): #Inner loop
          turtle.forward(side_length)
          turtle.left(90)


win = turtle.Screen()
tt = turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()


