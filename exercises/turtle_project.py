"""Turtle Project."""

__author__ = "730706009"


from turtle import Turtle, colormode, done
leo: Turtle = Turtle()


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    for _ in range(4):
        a_turtle.forward(width)
        a_turtle.right(90)


def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle with the specified radius at coordinates x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y - radius)
    a_turtle.pendown()
    a_turtle.circle(radius)


def draw_triangle(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw an equilateral triangle with the given side length at coordinates x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(60)  # Set the initial heading for an equilateral triangle
    a_turtle.pendown()
    for _ in range(3):
        a_turtle.forward(side_length)
        a_turtle.right(120)


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a rectangle with the given width and height at coordinates x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0)
    a_turtle.pendown()
    for _ in range(2):
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(height)
        a_turtle.right(90)


def main() -> None:
    """The entry point of my scene."""
    colormode(255)  # Set the color mode to use RGB values
    ertle = Turtle()
    ertle.pensize(2)
    ertle.speed(1)

    draw_square(ertle, -50, 50, 50)
    draw_circle(ertle, 50, 50, 30)
    draw_square(ertle, -50, -50, 40)
    draw_triangle(ertle, 50, -50, 60)
    draw_rectangle(ertle, -50, 0, 40, 80)

    ertle.hideturtle()
    done()


if __name__ == "__main__":
    main()