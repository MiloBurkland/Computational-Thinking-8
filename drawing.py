import turtle
from utils import*
import time
set_background("White background")
s1 = create_sprite("pen")
s1.pendown()
s1_colour = 0
def square_s1(s1):
    global s1_colour
    s1.speed(.01)
    s1.forward(100)
    s1.right(90)
    s1.forward(100)
    s1.right(90)
    s1.forward(100)
    s1.right(90)
    s1.forward(100)
    s1.right(100)
    window.update()
    time.sleep(0.001)

def square_s1_1(s1):
    global s1_colour
    s1.speed(0.01)
    s1.forward(200)
    s1.right(90)
    s1.forward(200)
    s1.right(90)
    s1.forward(200)
    s1.right(90)
    s1.forward(200)
    s1.right(200)
    window.update()
    time.sleep(0.001)

def square_s1_2(s1):
    global s1_colour
    s1.speed(0.01)
    s1.forward(150)
    s1.right(90)
    s1.forward(150)
    s1.right(90)
    s1.forward(150)
    s1.right(90)
    s1.forward(150)
    s1.right(90)
    window.update()
    time.sleep(0.001)

time.sleep(2)

for i in range(40):
    square_s1(s1)
    window.update()
    time.sleep(.001)

time.sleep(1)

for i in range(40):
    square_s1_1(s1)
    window.update()
    time.sleep(.001)

for i in range(40):
    square_s1_2(s1)
    window.update()
    time.sleep(.001)


window.update()
turtle.exitonclick()