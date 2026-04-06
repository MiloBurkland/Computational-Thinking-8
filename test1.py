from utils import *


set_background("Purple Spiral")

s1 = create_sprite("hand", 0, 40)
time.sleep(1)

def move_sprite_swirly_1(s1):
    s1.right(1)
    s1.forward(1)
    time.sleep(0.01)
    window.update()
def move_sprite_swirly_2(s1):
    s1.right(1)
    s1.forward(2)
    time.sleep(0.01)
    window.update()
def move_sprite_swirly_3(s1):
    s1.right(1)
    s1.forward(3)
    time.sleep(0.01)
    window.update()

while True:
    for a in range (10):
        move_sprite_swirly_1(s1)
    for b in range (10):
        move_sprite_swirly_2(s1)
    for c in range (10):
        move_sprite_swirly_3(s1)
    a = 0
    b = 0
    c = 0






window.update()
