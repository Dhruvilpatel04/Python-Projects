from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def rotate_clockwise():
    new_head = tim.heading()  - 10
    tim.setheading(new_head)
    
    
def rotate_anticlockwise():
    new_head = tim.heading() +10
    tim.setheading(new_head)
    

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_anticlockwise )
screen.onkey(key="c", fun= clear )

screen.exitonclick()