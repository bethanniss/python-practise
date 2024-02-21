import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit() :
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

print("I am thinking of a number between 0 and", top_of_range)
while True :
    user_guess = input("Guess the number:")
    guesses = guesses + 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Guess a number")
        continue 

    if user_guess == random_number:
        print("Well done!")
        break
    elif user_guess > random_number:
        print("You were above the number. Try again")
    else:
        print("You were below the number, try again")

if guesses > 1:
    print("You got it in", guesses, "guesses")
else:
    print("You got it in", guesses, "guess")

print("Play again?")
play_again = input("Y/N? ")
play_again = str(play_again)
if play_again == "Y":

else:
    quit()
    
 

