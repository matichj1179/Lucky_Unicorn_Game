import random

# set balance for testing purposes
balance = 5

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
    # if the random # is between 6 and 36
    # user gets a zebra (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # The token is either horse or zebra...
    # in both cases, subtract %0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print(f'You got a {chosen}, your balance is ${balance:.2f}')

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
print(f'Final Balance: ${balance:.2f}')
print("Thanks for playing")
