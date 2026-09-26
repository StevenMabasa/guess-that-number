import tkinter as tk
import random

secret_number = random.randint(1, 100)
#print(secret_number)
attempts = 0
limit = 5

def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    #print(secret_number)
    global attempts
    attempts = 0
    global limit
    limit = 5
    result.config(text="GAME RESTARTED, GOOD LUCK", fg="black")
    submit_button.config(state="normal")
    player_input.config(state="normal")
    player_input.delete(0, tk.END)

def end_game():
    submit_button.config(state="disabled")
    player_input.config(state="disabled")

def check_guess():
    global attempts
    global limit
    try:
        player_guess = int(player_input.get())
    except ValueError:
        result.config(text="Please enter a whole number.", fg="black")
        return
    if player_guess < 1 or player_guess > 100:
        result.config(text="Enter a number between 1 and 100 (1 and 100 are also included).", fg="black")
        return
    player_input.delete(0, tk.END)
    attempts += 1
    limit -= 1
    if player_guess > secret_number:
        result.config(text=f"{player_guess} is too high!\nGuesses left: {limit}", fg="black")
    elif player_guess < secret_number:
        result.config(text=f"{player_guess} is too low!\nGuesses left: {limit}", fg="black")
    else:
        if attempts > 1:
            result.config(text=f"YOU WIN, YOU GOT IT IN {attempts} ATTEMPTS!", fg="green")
        else:
            result.config(text=f"YOU WIN, YOU GOT IT IN {attempts} ATTEMPT!", fg="green")
        end_game()
        #submit_button.config(state="disabled")
        #player_input.config(state="disabled")
    if limit == 0 and player_guess != secret_number:
        result.config(text=f"GAME OVER, YOU LOSE! THE SECRET NUMBER WAS {secret_number}", fg="red")
        end_game()
        #submit_button.config(state="disabled")
        #player_input.config(state="disabled")
    

window = tk.Tk()
window.title("Guess That Number 🤩")
window.geometry("600x480")

rules = (
    "How to play:\n"
    "1. I'm thinking of a secret number from 1 to 100.\n"
    "2. Type your guess in the box and click \"Guess\".\n"
    "3. After each guess, I'll tell you if it's too high or too low.\n"
    "4. You only have 5 guesses. Run out, and it's game over!"
)

instruction = tk.Label(window, text=rules, justify="left", font=("Arial", 16, "bold"))
player_input = tk.Entry(window, width=20, font=("Arial", 14), justify="center")
submit_button = tk.Button(window, text="Guess", width=20, font=("Arial", 12, "bold"), command=check_guess)
result = tk.Label(window, text="GOOD LUCK", font=("Arial", 12, "bold"))
reset_button = tk.Button(window, text="New Game", width=20, font=("Arial", 12, "bold"), command=new_game)

instruction.pack()
player_input.pack(pady=50)
submit_button.pack()
result.pack(pady=50)
reset_button.pack()

window.mainloop()