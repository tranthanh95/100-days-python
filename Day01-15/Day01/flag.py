"""
Draw the flag with Python's turtle module
"""
import turtle

def draw_rectangle(x, y, width, height):
    """Draw a rectangle"""
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_star(x, y, radius):
    """Drawing a five-pointed star"""
    turtle.setpos(x, y)
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()


def  main ():
    """Main Program"""
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    # Draw the flag subject
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # Draw big stars
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # Draw little stars
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # Hidden Turtle
    Turtle.ht()
    # Show the drawing window
    turtle.mainloop()


if  __name__  ==  ' __main__ ' :
    main ()