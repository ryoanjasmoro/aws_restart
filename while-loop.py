# =========================
# Guess the Number Game
# =========================

import random  # import module untuk generate angka random

# Game intro
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Generate random number (1–10)
number = random.randint(1, 10)

# Flag untuk kontrol loop
isGuessRight = False

# While loop (akan terus jalan sampai benar)
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")

    # Validasi + logic
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))