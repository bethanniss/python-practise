print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Lets play!")
score = 0

print("Question 1")
answer1 = input("What colour is grass? ")

if answer1.lower() == "green":
    print("Correct! On to question 2")
    score = score + 1
else:
    print("Incorrect. Answer = green")

print("Question 2")
answer2 = input("How many days are in a year? ")

if answer2.lower() == "365":
    print("Correct! On to question 3")
    score = score + 1
else:
    print("Incorrect. Answer = 365")

print("Question 3")
answer3 = input("What is 7 x 7? ")

if answer3.lower() == "49":
    print("Correct! On to question 4")
    score = score + 1
else:
    print("Incorrect. Answer = 49")

print("Question 4")
answer4 = input("What does SQL stand for? ")
if answer4.lower() == "structured query language":
    print("Correct! End of quiz")
    score = score + 1
else:
    print("Incorrect. Answer = structured query language")

print("Well done! Here is your score: " + str(score) + " out of 4")

try_again = input("Would you like to try again? ")
if try_again != "yes":
    quit()


import random
r = random.randrange(-5,11)
print(r)





