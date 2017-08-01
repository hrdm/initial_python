import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("#FF007F", "red")
    brad.speed(1)

    for side in xrange(4):
        print(side)
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.color("green")

    for side in xrange(3):
        tom.forward(200)
        tom.right(120)

def draw_figures():
    window = turtle.Screen()
    window.bgcolor("#F6cc88")

    draw_square()
    draw_triangle()
    draw_circle()

    window.exitonclick()


draw_figures()
