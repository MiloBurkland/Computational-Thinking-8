yes = 0
no = 0

A1 = input(" I often fantasize about being powerful, successful, or admired. A) Agree. B) Neutral. C) Disagree. ")
if A1 == "A":
    yes = yes + 1
elif A1 == "C" or "B":
    no = no + 1

A2 = input(" When I know someone is struggling, I think of them often and hope they’re doing OK. A) Agree. B) Neutral. C) Disagree. ")
if A2 == "A":
    no = no + 1
elif A2 == "B" or "C":
    yes = yes + 1

A3 = input(" I don’t see a problem with lying if it helps me get what I want. A) Agree. B) Neutral. C) Disagree. ")
if A3 == "A":
    yes = yes + 1
elif A3 == "C":
    no = no + 1

A4 = input(" If someone told me that I hurt their feelings, I would feel badly. A) Agree. B) Neutral. C) Disagree. ")
if A4 == "A":
    no = no + 1
elif A4 == "B" or "C":
    yes = yes + 1
A5 = input(" Other people make so many stupid mistakes compared to me. A) Agree. B) Neutral. C) Disagree. ")
if A5 == "A":
    yes = yes + 1
elif A5 == "C":
    no = no + 1
A6 = input( "In truth, I find most people boring or stupid. A) Agree. B) Neutral. C) Disagree. ")
if A6 == "A" or "B":
    yes = yes + 1
elif A6 == "C":
    no = no + 1
A7 = input(" People often blame me for things that are actually their fault. A) Agree. B) Neutral. C) Disagree. ")
if A7 == "A":
    yes = yes + 1
elif A7 == "C":
    no = no + 1

























if yes > no:
    print("You have more chycapath aspects then not ")
elif no > yes:
    print("You only have a couple of pycopath aspects")



#https://www.psychologytoday.com/us/tests/personality/psychopathy-test