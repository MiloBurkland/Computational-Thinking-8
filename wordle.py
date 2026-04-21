import random
from words.py import word_list
# Pick a word at random
word_list = [word.txt]
hidden_word = random.choice(word_list)
print(f"{hidden_word}")
print("WORDLE:")

number_of_guesses = 1

# Repeat for 6 guesses
while number_of_guesses <= 6:
    # Guess a word
    guess_word = input("Guess a five letter word. ")
    output = ""
    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    
    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print(f"You win! It took you {number_of_guesses} guess. Good job")
        break

    else:
        print(" Try again")
        number_of_guesses += 1

print(f"Sorry you lost. The word was {hidden_word}. You will get it next time. " )

    