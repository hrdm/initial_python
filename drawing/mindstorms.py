import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("#F6cc88")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("#FF007F", "red")
    brad.speed(5)
    for i in xrange(1,37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angie - Draws a circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)

    window.exitonclick()

draw_art()
