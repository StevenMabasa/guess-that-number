# Guess That Number 🤩

A beginner-friendly number guessing game written in Python. The computer picks a secret number between 1 and 100, and you have **5 guesses** to find it. After each guess, the game tells you whether your guess was too high or too low.

The project includes two versions of the same game:

- **Desktop version** with a graphical window built using **tkinter**
- **Terminal version** that runs entirely in the command line

---

## Features

- Random secret number between 1 and 100 in every game
- "Too high" / "too low" hints after each guess
- A limit of 5 guesses, with the number of guesses left shown after each try
- Input validation: non-numbers and numbers outside 1–100 are rejected and don't use up a guess
- Colour-coded results: green for a win, red for game over
- A **New Game** button to play again without restarting the program (desktop version)

---

## How to Play

1. The game picks a secret number from 1 to 100.
2. Type your guess and click **Guess** (or press Enter in the terminal version).
3. The game tells you if your guess is too high or too low.
4. Find the number within 5 guesses to win. Run out of guesses, and it's game over!
5. In the desktop version, click **New Game** to play again.

---

## Requirements

- **Python 3.6 or newer** (download it from [python.org](https://www.python.org/downloads/))
- **tkinter** (needed for the desktop version only). It comes included with most Python installations.

No other packages are required. The game only uses Python's built-in `random` and `tkinter` modules.

To check that tkinter is installed, run:

```bash
python -m tkinter
```

If a small test window pops up, you're ready to go. If not, see [Troubleshooting](#troubleshooting).

---

## Getting the Project

### Option 1: Clone with Git

If you have [Git](https://git-scm.com/downloads) installed, run:

```bash
git clone https://github.com/your-username/guess-that-number.git
cd guess-that-number
```

### Option 2: Download as a ZIP

1. Go to the repository page on GitHub.
2. Click the green **Code** button, then **Download ZIP**.
3. Extract the ZIP file and open a terminal inside the extracted folder.

---

## Running the Game

Make sure your terminal is inside the project folder, then run one of the following.

**Desktop version (with a window):**

```bash
python guessing_game_gui.py
```

**Terminal version:**

```bash
python guessing_game.py
```

> **Note:** On macOS and Linux, you may need to type `python3` instead of `python`.

---

## Project Structure

```
guess-that-number/
├── guessing_game_gui.py   # Desktop version built with tkinter
├── guessing_game.py       # Terminal version
└── README.md              # This file
```

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'tkinter'`**

tkinter isn't installed with your copy of Python. Fix it for your system:

| System | Fix |
|---|---|
| Windows | Re-run the Python installer, choose **Modify**, and make sure **tcl/tk and IDLE** is ticked. |
| macOS | Install Python from [python.org](https://www.python.org/downloads/), which includes tkinter. With Homebrew: `brew install python-tk` |
| Linux (Ubuntu/Debian) | `sudo apt install python3-tk` |

**`python` is not recognized as a command**

Try `python3` instead. On Windows, you can also try `py`. If none of these work, Python may not be installed or may not have been added to your PATH during installation.

**The emoji in the window title shows up as a box**

Some systems (especially older Linux setups) can't display emojis in the title bar. This doesn't affect the game.

---

## What I Learned

This was my first project using tkinter. Building it taught me:

- Generating random numbers with the `random` module
- Using `while` loops, `break`, and `continue`
- Handling invalid input with `try` / `except`
- Creating windows and widgets (`Label`, `Entry`, `Button`) with tkinter
- Event-driven programming: connecting buttons to functions with `command=`
- Reading user input with `.get()` and updating the screen with `.config()`
- Using `global` to change variables inside functions
- Disabling and re-enabling widgets, and resetting game state

---

## Future Ideas

- Press Enter to submit a guess in the desktop version
- Track the best score across games
- Add difficulty levels (1–10, 1–100, 1–1000)
- Show a history of previous guesses
