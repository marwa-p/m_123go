# functions-----------------------------------------------------------------
import time

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Please enter your age in digits!")
       continue
    else:
       return userInput 
       break

def yes_no(question):
    valid = False
    while not valid:
        response = input (question).lower()

        if response == "yes" or response == "y":
            respose = "yes"
            return response
        
        elif response == "no" or response == "n":
            response = "no"
            return response 
        else:
            print("Please answer yes or no!")


def instructions():
    print ()
    print ()
    print("    ❀ ❀ ❀ How to play! ❀ ❀ ❀\n\n")
    time.sleep(1)
    print("You will be asked a question\n   and have 1 chance to answer\n  from one of the four options\n         a, b, c, or d.\n\n")
    time.sleep(2)
    print("°。°。°。°。°。°。°。°。°。°。°。°。°。")
    time.sleep(2)
    print("\n\n For every question you answer\n correctly you will be given a\n   specific amount of points,\n depending on the difficulty\n of the question\n")
    time.sleep(1)
    print("To win the game you need at\n   least 29 points, any lower\n        means you lost.")
    time.sleep(1)
    print("\n\n    ❀ ❀ ❀ Good Luck! ❀ ❀ ❀ ")
    time.sleep(2)

    print()

# main ----------------------------------------------------------------------


print("\n ❖ ❖ Welcome to 123 Go! ❖ ❖")
time.sleep(1)

# Ask user for name

name = input("What is your name? ➸ ")


print(f" \n\n✦ Welcome, {name}! ✦")
age = inputNumber("\n\nWhat is your age? ➸ ")

# Ask user for age

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Please enter your age in digits! ➸ ")
       continue
    else:
       return userInput 
       break

# If user hasn't played before, display instructions. If they have, skip.

show_instructions = yes_no("\nHave you played this game before? ➸  ")
print ()
print ("You chose {}".format(show_instructions))

if show_instructions == "no":
    instructions()

print()
time.sleep(1)

print ("  ✧  Here are your 10 questions. ✧ \n     Answer with a, b, c, or d...")
print("\n●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
print()
print()
print()
time.sleep(1)

# Give user only 1 chance to answer correctly
chances = 1


# Start score as 0
score = 0

# Print questions, if correct give specified amount of points, if wrong give no points

#Q1 ---------------------------------------------------------------------------
time.sleep(1)
question_1 = print("1) 10 x 4 = 26 + ?\n"
                   "(a) 13\n"
                   "(b) 14\n"
                   "(c) 15\n"
                   "(d) 16\n\n ")
answer_1 = "b"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_1):
        score = score + 10
        print("Correct! You have earned 10 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break

print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
    
time.sleep(1)




#Q2 ---------------------------------------------------------------------------
question_2 = print("2) How many faces does a triangular prism have?\n"
                   "(a) 5\n"
                   "(b) 3\n"
                   "(c) 7\n"
                   "(d) 9\n\n ")
answer_2 = "a"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_2):
        score = score + 7
        print("Correct! You have earned 7 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break



print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")

time.sleep(1)




#Q3 ---------------------------------------------------------------------------
question_3 = print("3) How many degrees do angles around a point add up to?\n"
                   "(a) 360\n"
                   "(b) 180\n"
                   "(c) 90\n"
                   "(d) 70\n\n ")
answer_3 = "a"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_3):
        score = score + 4
        print("Correct! You have earned 4 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break


print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")

time.sleep(1)




#Q4 ---------------------------------------------------------------------------
question_4 = print("4) (4+7)x3= ?\n"
                   "(a) 29\n"
                   "(b) 30\n"
                   "(c) 31\n"
                   "(d) 33\n\n ")
answer_4 = "d"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_4):
        score = score + 10
        print("Correct! You have earned 10 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break



print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")

time.sleep(1)




#Q5 ---------------------------------------------------------------------------
question_5 = print("5) (36/6)-10= ?\n"
                   "(a) -8\n"
                   "(b) -4\n"
                   "(c) 4\n"
                   "(d) 8\n\n ")
answer_5 = "b"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_5):
        score = score + 8
        print("Correct! You have earned 8 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
time.sleep(1)
#Q6 ---------------------------------------------------------------------------
question_6 = print("6) 5^2 = ?\n"
                   "(a) 10\n"
                   "(b) 25\n"
                   "(c) 7\n"
                   "(d) 3\n\n ")
answer_6 = "b"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_6):
        score = score + 3
        print("Correct! You have earned 3 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
time.sleep(1)
#Q7 ---------------------------------------------------------------------------
question_7 = print("7) What is 3/7 of 35\n"
                   "(a) 13\n"
                   "(b) 14\n"
                   "(c) 15\n"
                   "(d) 16\n\n ")
answer_7 = "c"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_7):
        score = score + 5
        print("Correct! You have earned 5 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
time.sleep(1)
#Q8 ---------------------------------------------------------------------------
question_8 = print("8) How many cm are in 7m?\n"
                   "(a) 0.7\n"
                   "(b) 7\n"
                   "(c) 70\n"
                   "(d) 700\n\n ")
answer_8 = "d"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_8):
        score = score + 1
        print("Correct! You have earned 1 point.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
time.sleep(1)
#Q9 ---------------------------------------------------------------------------
question_9 = print("9) What is nine squared?\n"
                   "(a) 99\n"
                   "(b) 18\n"
                   "(c) 81\n"
                   "(d) 11\n\n ")
answer_9 = "c"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_9):
        score = score + 8
        print("Correct! You have earned 8 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
time.sleep(1)
#Q10 ---------------------------------------------------------------------------
question_10 = print("10) In the number 37,812,645 what is the digit in the one million's place?\n"
                   "(a) 7\n"
                   "(b) 2\n"
                   "(c) 8\n"
                   "(d) 6\n\n ")
answer_10 = "c"

for i in range(chances):
    answer = input(" Your answer ➸ ")
    if (answer.lower() == answer_10):
        score = score + 2
        print("Correct! You have earned 2 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")
    break
print("●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・○・●・\n")
time.sleep(1)
# Game ends once all 10 questions have been asked and answered



# Print the total score, if above or equal to 29, say well done, if it's lower say better luck next time.

while score >= 29:
    print(f" ❃❃ Well done {name}! ❃❃\n Your score is ⇉", score)
    break

while score <= 28:
    print("Your score is", score)
    print(f" ❃❃ Better luck next time, {name}! ❃❃" )
    break

#Print goodbye message
print("\n\n ✦ Thank you for playing 123 Go! We hope to see you again :) ✦ ")







