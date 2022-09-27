# functions-----------------------------------------------------------------

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
            print("Please answer yes or no")


def instructions():
    print ()
    print ()
    print("***** How to Play *****")
    print()
    print(" instructions here ")


# main ----------------------------------------------------------------------


txt = input("\nWelcome to 123 Go! What is your name? ")
print(f"Welcome, {txt}")


show_instructions = yes_no("Have you played this game before?   ")
print ()
print ("You chose {}".format(show_instructions))

if show_instructions == "no":
    instructions()

print()

print ("Program continues...")
print()
print()
print()

 





