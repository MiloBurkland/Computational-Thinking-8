from utils import *
set_background("spring")

#topright
s2 = create_sprite("cardinal", 100, 150)
s2 = create_sprite("cardinal", 100, 149)
s2 = create_sprite("cardinal", 100, 148)
s2 = create_sprite("cardinal", 100, 147)
s2 = create_sprite("cardinal", 100, 146)
s2 = create_sprite("cardinal", 100, 145)

#topleft
s2 = create_sprite("cardinal", -100, 150)
s2 = create_sprite("cardinal", -100, 149)
s2 = create_sprite("cardinal", -100, 148)
s2 = create_sprite("cardinal", -100, 147)
s2 = create_sprite("cardinal", -100, 146)
s2 = create_sprite("cardinal", -100, 145)

#bottomleft
s2 = create_sprite("cardinal", -100, -150)
s2 = create_sprite("cardinal", -100, -149)
s2 = create_sprite("cardinal", -100, -148)
s2 = create_sprite("cardinal", -100, -147)
s2 = create_sprite("cardinal", -100, -146)
s2 = create_sprite("Dragon brown", -100, -145)

message1 = create_sprite("alien",-200,200)
message1.color("yellow")
message1.write("Hi Milo",font = ("Times New Roman", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()