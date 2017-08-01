import turtle

# def draw_triangle(some_turtle, side_len):
#     some_turtle.begin_fill()
#     for side in xrange(3):
#         some_turtle.forward(side_len)
#         some_turtle.left(120)
#     some_turtle.end_fill()

def draw_triangle(some_turtle, side_len):
    some_turtle.begin_fill()
    some_turtle.left(60)
    some_turtle.forward(side_len)
    for side in xrange(2):
        some_turtle.right(120)
        some_turtle.forward(side_len/2)
    for side in xrange(2):
        some_turtle.left(120)
        some_turtle.forward(side_len/2)
    for side in xrange(2):
        some_turtle.right(120)
        some_turtle.forward(side_len/2)
    some_turtle.forward(side_len/2)
    some_turtle.end_fill()
    some_turtle.right(180)

def draw_fractal_x2(some_turtle, side_len):
    draw_triangle(some_turtle,side_len)
    some_turtle.left(60)
    some_turtle.forward(side_len)
    some_turtle.right(60)
    draw_triangle(some_turtle,side_len)
    some_turtle.right(60)
    some_turtle.forward(side_len)
    some_turtle.left(60)
    draw_triangle(some_turtle,side_len)
    some_turtle.forward(-side_len)

def draw_fractal_x4(some_turtle, side_len):
    draw_fractal_x2(some_turtle,side_len/2)
    some_turtle.left(60)
    some_turtle.forward(side_len)
    some_turtle.right(60)
    draw_fractal_x2(some_turtle,side_len/2)
    some_turtle.right(60)
    some_turtle.forward(side_len)
    some_turtle.left(60)
    draw_fractal_x2(some_turtle,side_len/2)
    some_turtle.forward(-side_len)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("#F6cc88")

    tom = turtle.Turtle()
    tom.shape("turtle")
    tom.color("blue","#00ff80")
    tom.speed(3)
    draw_fractal_x4(tom,4*40)

    window.exitonclick()

draw_art()






#Create the turtle Brad - Draws a square
# brad = turtle.Turtle()
# brad.shape("turtle")
# brad.color("#FF007F", "red")
# brad.speed(10)
# for i in xrange(1,360):
#     # draw_square(bra       d)
#     draw_rumble(brad)
#     brad.right(1)

#Create the turtle Angie - Draws a circle
# angie = turtle.Turtle()
# angie.shape("arrow")
# angie.color("blue")
# angie.circle(100)

# draw_triangle(100)

#
# def draw_square(some_turtle):
#     for i in range(1,5):
#         some_turtle.forward(100)
#         some_turtle.right(90)




# def draw_rumble(some_turtle):
#     some_turtle.right(100)
#     some_turtle.forward(100)
#     some_turtle.left(20)
#     some_turtle.forward(100)
#     some_turtle.left(160)
#     some_turtle.forward(100)
#     some_turtle.left(20)
#     some_turtle.forward(100)

# def draw_triangle(side_len):
#     tom = turtle.Turtle()
#     tom.shape("turtle")
#     tom.color("blue","#00ff80")
#     tom.speed(2)
#     tom.begin_fill()
#     for side in xrange(3):
#         tom.forward(side_len)
#         tom.left(120)
#     tom.end_fill()
