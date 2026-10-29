import turtle

screen = turtle.Screen()
screen.title("Mini Drawing App")
screen.bgcolor("white")
screen.setup(width=800, height=600)

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.pensize(3)

colors = ["red", "blue", "green", "purple", "orange"]
color_index = 0


def move_forward():
    pen.forward(30)


def turn_left():
    pen.left(30)


def turn_right():
    pen.right(30)


def change_color():
    global color_index
    color_index = (color_index + 1) % len(colors)
    pen.color(colors[color_index])


def draw_circle():
    pen.circle(50)


def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(change_color, "c")
screen.onkey(draw_circle, "space")
screen.onkey(clear_screen, "x")

print("Mini Drawing App Controls:")
print("Up Arrow  - Move forward")
print("Left/Right - Turn")
print("C         - Change color")
print("Space     - Draw a circle")
print("X         - Clear drawing")
print("Close the window to exit.")

turtle.done()
```
