#Importing
import turtle
import time
from utils import*

#This game is meant to test your skills at keeping someone alive by controlling there medicine and oxygen:

#time tracking
start = time.time()

#creating background and sprites
set_background("Hospital")
s1 = create_sprite("Man", -100,50)

s2 = create_sprite("dot", -300,200)
s2.hideturtle()

s3 = create_sprite("dot", -300,185)
s3.hideturtle()

s4 = create_sprite("dot", -300,170)
s4.hideturtle()

s5 = create_sprite("dot", -100, 0)
s5.hideturtle

#making variables
s1_health = 5
s1_meds = 10
s1_oxygen = 50
person_alive  = 1
Health_loss = 5
oxygen_imbalence_counter = 0
med_imbalence_counter =0
time_since_loss_o = 0
time_since_loss_m = 0

#displaying variables
def alien_write_variabels1(s2):
    global s1_health
    s2.color("pink")
    s2.clear()
    s2.write(f" Current health: {s1_health}. Try to stay alive!",font = ("Times New Roman", 10, "normal"))
    window.update()

def alien_write_variabels2(s3):
    global s1_oxygen
    s3.color("purple")
    s3.clear()
    s3.write(f" Current oxygen: {s1_oxygen} (Click o for increase. Don't go under 35 or over 65!)",font = ("Times New Roman", 10, "normal"))
    window.update()

def alien_write_variabels3(s4):
    global s1_meds
    s4.color("green")
    s4.clear()
    s4.write(f" Current medicine: {s1_meds} (Press m for increase. Don't go under 5 or over 15! )",font = ("Times New Roman", 10, "normal"))
    window.update()

#A all in one
def alien_write_variabels():
    alien_write_variabels1(s2)
    alien_write_variabels2(s3)
    alien_write_variabels3(s4)
    window.update()

#Manedging oxygen
def oxygen_work():
    global oxygen_imbalence_counter, s1_oxygen, time_since_loss_o
    time_since_loss_o += 1
    if s1_oxygen < 35 or s1_oxygen > 65:
        oxygen_imbalence_counter += 1
    
    if time_since_loss_o >= 6:
        s1_oxygen -= 1
        time_since_loss_o = 0

    alien_write_variabels()

#maneging meds
def meds_work():
    global s1_meds, med_imbalence_counter, time_since_loss_m
    time_since_loss_m += 1
    if s1_meds < 5 or s1_meds > 15:
        med_imbalence_counter += 1
    
    if time_since_loss_m >= 10:
        s1_meds -= 1
        time_since_loss_m = 0
    
    alien_write_variabels()

#clicking
def oxygen_click():
    global s1_oxygen
    s1_oxygen += 1

def meds_click():
    global s1_meds
    s1_meds += 1

#adding to Health_loss and losing s1_health
def H_l_plus():
    global Health_loss
    Health_loss += 0.7
    alien_write_variabels()
    window.update()

#losing s1_health
def s_h_loss():
    global s1_health
    s1_health -= 0.05
    alien_write_variabels()
    window.update()


#How losing health works
def health_loss():
    global Health_loss
    global s1_meds
    global s1_oxygen
    if Health_loss > 0:
        Health_loss -= 0.5
    
    else:
        s1_health -= 1
        Health_loss = 5
    
    if s1_oxygen > 35 and s1_oxygen < 65:
        H_l_plus()
    
    elif s1_oxygen < 35 or s1_oxygen > 65:
        s_h_loss()
    
    if s1_meds > 5 and s1_meds < 15:
        H_l_plus()
    
    elif s1_meds < 5 or s1_meds > 15:
        s_h_loss()

#losing game message
def losing_game_message():
    global elapsed
    global person_alive
    elapsed = time.time() - start
    s1.write("You lost. Sorry.",font = ("Times New Roman", 10, "normal"))
    if elapsed > 60:
        s5.write(f"You lasted {elapsed:.2f} seconds. Good job!",font = ("Times New Roman", 10, "normal"))
    elif elapsed < 60:
        s5.write(f"You lasted {elapsed:.2f} seconds. Not great try again.",font = ("Times New Roman", 10, "normal"))
    person_alive += 1
    window.update()
    time .sleep(8)
    turtle.bye() 


#How to lose the game
def losing_game():
    global oxygen_imbalence_counter
    global med_imbalence_counter
    global s1_health
    global elapsed
    global start
    if s1_health <= 0:
        losing_game_message()

    elif oxygen_imbalence_counter >= 45:
        losing_game_message()
    
    elif med_imbalence_counter >= 45:
        losing_game_message() 

#function that goes in loop
def All_Functions():
    alien_write_variabels()
    health_loss()
    losing_game()
    oxygen_work()
    meds_work()
    window.update
    time.sleep(0.04)

alien_write_variabels()

time.sleep(3)

#key pressing
window.onkeypress(oxygen_click, "o")
window.onkeypress(meds_click, "m")
window.listen()

while True:
    All_Functions()



turtle.done()