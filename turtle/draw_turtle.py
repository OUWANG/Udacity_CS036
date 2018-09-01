import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(1,30):
        brad.forward(20)
        brad.circle(30)
        for j in range(1,5):
            brad.stamp()
            brad.forward(15)
        brad.right(30)
    window.exitonclick()

draw_square()
