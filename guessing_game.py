import random

secret_number = random.randint(1, 100)
#print(f"Secret number is: {secret_number}")
attempts = 0
limit = 5

while limit > 0:
    try:
        player_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue
    if player_guess < 1 or player_guess > 100:
        print("Enter a number between 1 and 100 (1 and 100 are also included).")
        continue
    else:
        attempts += 1
        limit -= 1
        #print(f"You guessed: {player_guess}")
        if player_guess > secret_number:
            print("Too high!")
        elif player_guess < secret_number:
            print("Too low!")
        else:
            if attempts > 1:
                print(f"You got it in {attempts} attempts!")
            else:
                print(f"You got it in {attempts} attempt!")
            break

if limit == 0 and player_guess != secret_number:
    print(f"GAME OVER, YOU LOSE! The secret number was {secret_number}")