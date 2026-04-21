Winter=0

Spring=0

Summer=0

Fall=0

print("")

Question1=input("What is your favorite type of weather: A) Cool and rainy B) Hot and sunny C) Crisp and windy D) Cold and snowy ")

if Question1 == "D":

   Winter += 1

elif Question1 == "B":

   Summer += 1

elif Question1 == "A":

   Fall += 1

elif Question1 == "C":

   Spring += 1

print("")
input("")
print("")

Question2=input ("What do you like to do: A) Watching flowers bloom B) Swimming or going to the beach C) Walking through colorful leaves D) Drinking hot chocolate indoors ")

if Question2== "A":

   Spring += 1

elif Question2== "B":

   Summer += 1

elif Question2== "C":

   Fall += 1

elif Question2== "D":

   Winter += 1

print("")
input("")
print("")

Question3=input("Pick a vibe: A) Bright, energetic, social B) Calm, cozy, thoughtful C) Quiet, peaceful, reflective D) Fresh, hopeful, motivated ")

if Question3 == "A":

   Summer += 1

elif Question3 == "B":

   Fall += 1

elif Question3 == "C":

   Winter += 1

elif Question3 == "D":

   Spring += 1

print("")
input("")
print("")

Question4=input("Choose a smell A) Sunscreen or ocean air B) Cinnamon or coffee C) Snow or pine D) Fresh rain or flowers ")

if Question4 == "A":

   Summer += 1

elif Question4 == "B" or "b":

   Fall += 1

elif Question4 == "C" or "c":

   Winter += 1

elif Question4 == "D" "d":

   Spring += 1

print("")
input("")
print("")

Question5=input("Energy? A) High · B) Grounded · C) Calm · D) Hopeful ")

if Question5 == "A" or "a":

   Summer += 1

elif Question5 == "B" or "b":

   Fall += 1

elif Question5 == "C" or "c":

   Winter += 1

elif Question5 == "D" "d":

   Spring += 1

print("")
input("")
print("")

Question6=input("Colors? A) Bright · B) Warm · C) Cool · D) Paste ")

if Question6 == "A" or "a":

   Summer += 1

elif Question6 == "B" or "b":

   Fall += 1

elif Question6 == "C" or "c":

   Winter += 1

elif Question6 == "D" or "d":

   Spring += 1

print("")
input("")
print("")

if Winter > Spring and Winter > Fall and Winter > Summer:

   print("You are a Winter person ")

elif Spring > Winter and Spring > Fall and Spring >Summer:

   print("You are a Spring person ")

elif Fall > Winter and Fall > Spring and Fall > Summer:

   print ("You are a Fall person ")

elif Summer > Winter and Summer > Spring and Summer > Fall:
   
   print("You are a Summer person ")

elif Winter and Spring and Fall and Summer == Winter and Spring and Fall and Summer:
   print("You got mixed results ")

else:
   print("Something went wrong please try again ")




























