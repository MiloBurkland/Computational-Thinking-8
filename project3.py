from utils import*
import random
import time
#Making sprites and background
set_background("Purple Spiral")
s1 = create_sprite("hand", -200, 230)
s2 = create_sprite("hand", -200, 80)
s3 = create_sprite("hand", -200, -100)
s4 = create_sprite("hand", -200, -240)
#pmts1 stands for pixels moved toward s1
pmts1 = 0
pmts2 = 0
pmts3 = 0
pmts4 = 0
number_wins_any = 0
time.sleep(1)
#loop for large random result

    #defining movement
def s1_move(s1):
    global pmts1
    #they all have same random range
    s1_forward = random.randint(1,5)
    #pmts1 stands for pixels moved toward s1
    s1.forward(s1_forward)
    time.sleep(0.01)
    if s1_forward == 1:
        pmts1 += 1
    if s1_forward == 2:
        pmts1 += 2
    if s1_forward == 3:
        pmts1 += 3
    if s1_forward == 4:
        pmts1 += 4
    if s1_forward == 5:
        pmts1 += 5
    window.update()
def s2_move(s2):
    global pmts2
    s2_forward = random.randint(1,5)
    s2.forward(s2_forward)
    time.sleep(0.01)
    if s2_forward == 1:
        pmts2 += 1
    if s2_forward == 2:
        pmts2 += 2
    if s2_forward == 3:
        pmts2 += 3
    if s2_forward == 4:
        pmts2 += 4
    if s2_forward == 5:
        pmts2 += 5
    window.update()

def s3_move(s3):
    global pmts3
    s3_forward = random.randint(1,5)
    s3.forward(s3_forward)
    time.sleep(0.01)
    if s3_forward == 1:
        pmts3 += 1
    if s3_forward == 2:
        pmts3 += 2
    if s3_forward == 3:
        pmts3 += 3
    if s3_forward == 4:
        pmts3 += 4
    if s3_forward == 5:
        pmts3 += 5
    window.update()

def s4_move(s1):
    global pmts4
    s4_forward = random.randint(1,5)
    s4.forward(s4_forward)
    time.sleep(0.01)
    if s4_forward == 1:
        pmts4 += 1
    if s4_forward == 2:
        pmts4 += 2
    if s4_forward == 3:
        pmts4 += 3
    if s4_forward == 4:
        pmts4 += 4
    if s4_forward == 5:
        pmts4 += 5
    window.update()
    #loop for movement
sprites_wins2 = 0
for i in range(120):
    s1_move(s1)
    s2_move(s2)
    s3_move(s3)
    s4_move(s1)
    window.update
    #calculating who won
    if pmts1 >= 375:
        s1.write(" Top Hand won this round! ", font = ("Arial", 20, "normal"))
        sprites_wins2 += 1
        window.update()
    if pmts2 >= 375:
        s2.write(" Middle top Hand won this round! ", font = ("Arial", 20, "normal"))
        sprites_wins2 += 1
        window.update()
    if pmts3 >= 375:
        s3.write(" Bottom middle Hand won this round! ", font = ("Arial", 20, "normal"))
        sprites_wins2 += 1
        window.update()
    if pmts4 >= 375:
        s4.write(" Bottom Hand won this round! ", font = ("Arial", 20, "normal"))
        window.update()
    window.update()

window.update()
turtle.exitonclick()