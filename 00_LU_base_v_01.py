# Functions go here

# Checks user answer yes / no to a question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


# Displays instructions, returns ""
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game goes here")
    print()
    return ""


# Checks user enters an integer between a low and high number
def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

print("program continues")

# Ask user how much the want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)
print(f'You chose ${how_much:.2f}')
