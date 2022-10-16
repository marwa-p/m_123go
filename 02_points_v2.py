#Chances
chances = 1
print("You only have", chances, "chance to answer correctly! \n The answers are multichoice, please answer according to the letter with each answer\n")


#Score
score = 0

#Q1 ---------------------------------------------------------------------------
question_1 = print("1) 10 x 4 = 26 + ?\n"
                   "(a) 13\n"
                   "(b) 14\n"
                   "(c) 15\n"
                   "(d) 16\n\n ")
answer_1 = "b"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_1):
        score = score + 10
        print("Correct! You have earned 10 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")



#Q2 ---------------------------------------------------------------------------
question_2 = print("2) How many faces does a triangular prism have?\n"
                   "(a) 5\n"
                   "(b) 3\n"
                   "(c) 7\n"
                   "(d) 9\n\n ")
answer_2 = "a"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_2):
        score = score + 7
        print("Correct! You have earned 7 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")





#Q3 ---------------------------------------------------------------------------
question_3 = print("3) How many degrees do angles around a point add up to?\n"
                   "(a) 360\n"
                   "(b) 180\n"
                   "(c) 90\n"
                   "(d) 70\n\n ")
answer_3 = "a"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_3):
        score = score + 4
        print("Correct! You have earned 4 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")





#Q4 ---------------------------------------------------------------------------
question_4 = print("4) (4+7)x3= ?\n"
                   "(a) 29\n"
                   "(b) 30\n"
                   "(c) 31\n"
                   "(d) 33\n\n ")
answer_4 = "d"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_4):
        score = score + 10
        print("Correct! You have earned 10 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")






#Q5 ---------------------------------------------------------------------------
question_5 = print("5) (36/6)-10= ?\n"
                   "(a) -8\n"
                   "(b) -4\n"
                   "(c) 4\n"
                   "(d) 8\n\n ")
answer_5 = "b"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_5):
        score = score + 8
        print("Correct! You have earned 8 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")


#Q6 ---------------------------------------------------------------------------
question_6 = print("6) 5^2 = ?\n"
                   "(a) 10\n"
                   "(b) 25\n"
                   "(c) 7\n"
                   "(d) 3\n\n ")
answer_6 = "b"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_6):
        score = score + 3
        print("Correct! You have earned 3 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")


#Q7 ---------------------------------------------------------------------------
question_7 = print("7) What is 3/7 of 35\n"
                   "(a) 13\n"
                   "(b) 14\n"
                   "(c) 15\n"
                   "(d) 16\n\n ")
answer_7 = "c"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_7):
        score = score + 5
        print("Correct! You have earned 5 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")


#Q8 ---------------------------------------------------------------------------
question_8 = print("8) How many cm are in 7m?\n"
                   "(a) 0.7\n"
                   "(b) 7\n"
                   "(c) 70\n"
                   "(d) 700\n\n ")
answer_8 = "b"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_8):
        score = score + 1
        print("Correct! You have earned 1 point.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")


#Q9 ---------------------------------------------------------------------------
question_9 = print("9) What is nine squared?\n"
                   "(a) 99\n"
                   "(b) 18\n"
                   "(c) 81\n"
                   "(d) 11\n\n ")
answer_9 = "c"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_9):
        score = score + 8
        print("Correct! You have earned 8 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")


#Q10 ---------------------------------------------------------------------------
question_10 = print("10) In the number 37,812,645 what is the digit in the one million's place?\n"
                   "(a) 7\n"
                   "(b) 2\n"
                   "(c) 8\n"
                   "(d) 8\n\n ")
answer_10 = "d"

for i in range(chances):
    answer = input("Your answer: ")
    if (answer.lower() == answer_10):
        score = score + 2
        print("Correct! You have earned 2 points.\n")
        break
    else:
        print("Incorrect! The correct answer is", answer_1, "\n\n")

# Questions end ---------------------------------------------------------------------



#print the score
while score >= 29:
    print("Well done! Your score is", score)
    break

while score <= 28:
    print("Your score is", score, "Better luck next time!" )
    break
#Goodbye message
print("Thank you for playing 123 Go! We hope to see you again :)")
