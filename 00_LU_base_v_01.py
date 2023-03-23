import random


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


def statement_generator(statement, decoration, lines=1):
    sides = decoration * 5

    middle = f"{sides} {statement} {sides}"
    top_bottom = f"{decoration * len(middle)}"

    if lines == 1:
        print(middle)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main Routine goes here
# Display heading
statement_generator("Welcome to lucky Unicorn ", "*", 5)

# Display instructions if requested
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

# Ask user how much the want to play with
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("press <enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print(f'*** round #{rounds_played} ***')
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        statement_generator("You got a unicorn", "!", 3)

    # if the random # is between 6 and 36
    # user gets a zebra (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        statement_generator("You got Donkey", "🐎")

    # The token is either horse or zebra...
    # in both cases, subtract %0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            statement_generator("You got a Horse", "🐴")
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            statement_generator("You got a Zebra", "🦓")

        balance -= 0.5

    print(f'You got a {chosen}, your balance is ${balance:.2f}')

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
statement_generator("Results", "=")
print()
print(f'Final Balance: ${balance:.2f}')
print("Thanks for playing")
