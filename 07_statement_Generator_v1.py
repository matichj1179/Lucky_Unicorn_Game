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


statement_generator("You got a unicorn", "!", 3)
print()
statement_generator("You got a Zebra", "🦓")
