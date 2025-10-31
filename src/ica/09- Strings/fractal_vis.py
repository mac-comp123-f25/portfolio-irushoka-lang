import turtle


# L-system is a set of rules that repeatedly replace symbols to generate a string,
# which can then be interpreted as a drawing


#You start with a simple symbol or word (the axiom).
#You have rules that say: “replace this symbol with this sequence of symbols.”
#Each iteration applies the rules to every symbol in the current word.
def generate_lsystem(axiom, rules, iterations):
    """
    Generate the L-system string after a number of iterations.
    """
    result = axiom
    for _ in range(iterations):
        new_result = ""
        for char in result:
            new_result += rules.get(char, char)
        result = new_result
    return result


# --- Curve 1: Koch Curve ---
def koch_curve(t, length, iterations):
    """
    Draw the Koch curve using Turtle.
    n = 4
    axiom = 'F'
    rule = F -> F+F--F+F
    angle δ = 60°
    scale factor s = 1/3
    """
    axiom = "F"
    rules = {"F": "F+F--F+F"}
    angle = 60
    instructions = generate_lsystem(axiom, rules, iterations)

    for move in instructions:
        if move == "F":
            t.forward(length)
        elif move == "+":
            t.left(angle)
        elif move == "-":
            t.right(angle)


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-300, 0)
    t.pendown()
    koch_curve(t, 5, 4)  # length=5, 4 iterations

    turtle.done()

if __name__ == "__main__":
    main()