<div align="center">
  <a href="https://bjorne90.github.io/math-games-for-children/index.html" target="_blank">
    <img src="assets/images/logo.jpg" alt="Logo" width="250" height="100">
  </a>

  <h3 align="center">Project 4 - HR Mangament</h3>

  <p align="center">
    My Python project for Code Institute. A Battleship game.
    <br />
    <br />
    <a href="https://battleship-game-bc.herokuapp.com/" target="_blank">View Demo Website</a>
  </p>
</div>

## Table of Contents
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Features">Features</a></li>
    <li><a href="#How-to-Play">How to Play</a></li>
    <li><a href="#Game-Instructions">Game Instructions</a></li>
    <li><a href="#Scoring">Scoring</a></li>
    <li><a href="#Known-Bugs-and-Fixes">Known Bugs and Fixes</a></li>
    <li><a href="#Data-Model">Data Model</a></li>
    <li><a href="#Validating-&-Testing">Validating & Testing</a></li>
    <li><a href="#Credits">Credits</a></li>
  </ol>
</details>
<br />


# Python Battleship Game 🗺️

Battleship is a classic grid-based strategy game where the player competes against the computer by guessing the locations of its hidden fleet of ships. The objective is to sink all of the computer's ships within a limited number of turns.

![Mockup of the game](assets/images/mockup.png)

# Features

- Choose between three difficulty levels: easy, medium, and hard
- Random ship placement for the computer's fleet
- Customizable fleet configuration and grid size based on the chosen difficulty level
- Score tracking and leaderboard to save top 10 players' scores
- Age and name input for a more personalized experience
- Reads and writes name, age and score to Google Sheet

  ![Features of the game](assets/images/features4.png)

---

## How to Play

1. Clone or download this repository
2. Run the Battleship game in a Python 3 environment using the following command: `python battleship.py`
3. Follow the on-screen instructions to provide your name, age, and desired difficulty level
4. Start guessing the locations of the computer's ships by entering the row and column numbers
5. Try to sink all of the computer's ships within the given number of turns
6. You can also play it via [Demo Link](https://battleship-game-bc.herokuapp.com/) in the top of whis README

![Fun Math Game Screenshot 2](assets/images/howtoplay.png)

---

## Game Instructions

1. In this game, you'll try to sink a fleet of ships hidden on a grid by guessing their positions.
2. You'll have a limited number of turns to guess their locations, and the game will show you whether your guess was a hit, miss, or a duplicate guess.
3. To make a guess, enter the row and column of the cell you want to target.
4. Good luck!

---

## Scoring

Players earn points for each successful hit. The points earned for a hit depend on the type of ship hit and the ship's size. The top 10 players' scores will be displayed on the scoreboard.

![Scoreboard of the game](assets/images/scores.png)

---

## Known Bugs and Fixes

* Write name, age and score to the top 10 list **(*Solved*)**
* No information came out to the leaderboard **(*Solved*)**
* Syntax error when game ended, no information saved **(*Solved*)**
* The gameboard was flashing turing play, trying to change os.system to termclear, without result.
  Fixing it by make *'guess_row, guess_col = user_guess(player_board)'* inside the *'while turns > 0:' loop.* **(*Solved*)**
* The top 10 scoreboard dont show when player wins by sinking all ships **(*Solved*)**
* The computers score if there are a hit is not always showing **(*Not Solved, look at the image in #scoring*)**

* A fix for the code is to make the *def main():* shorter. I haven't found a workaround for it yet. **(*In progress*)**

---

## Data Models

The Battleship game is designed with the following data model:

### UserProfile

*The UserProfile model represents additional user profile information:*

* `user` : One-to-one relationship with the User model from Django's built-in authentication system.
* `phone_number` : CharField to store the user's phone number.
* `address` : CharField to store the user's address.
* `booked_workshifts` : Many-to-many relationship with the `Booking` model from the booking app to represent the workshifts booked by the user.

### Ship

*A Ship object represents a ship on the game board. It has the following attributes:*

* name (str): The name of the ship.
* size (int): The size of the ship (in grid units).
* hits (int): The number of times the ship has been hit.

### Board

A Board object represents a game board. It has the following attributes:

* size (int): The size of the board (in grid units).
* ships (list): A list of Ship objects on the board.
* grid (list): A 2D list representing the state of the board. Each element in the grid can be one of the following:
    * "0": An empty cell.
    * "S": A cell containing part of a ship.
    * "H": A cell containing a part of a ship that has been hit.
    * "M": A cell that has been fired at and missed.

### Game

A Game object represents a game instance. It has the following attributes:

* player (Player): The player object for the game.
* board_size (int): The size of the game board.
* difficulty (str): The difficulty level of the game ("easy", "medium", or "hard").
* player_board (Board): The player's game board.
* computer_board (Board): The computer's game board.
* fleet (list): A list of tuples representing the ships in the game fleet. Each tuple contains the size of the ship and its name.
* turns (int): The number of turns the player has to sink all the ships.
* ship_points (dict): A dictionary mapping ship names to their point values.
* hits (dict): A dictionary mapping ship names to the number of hits they have received.
* total_ship_sizes (int): The sum of the sizes of all the ships in the game fleet.
* score (int): The player's score.
* computer_score (int): The computer's score.

### Functions

The following functions are defined in the module:

* place_random_fleet(board, fleet): Places the ships in the fleet randomly on the given board.
* user_guess(board): Prompts the user for a guess on the given board.
* check_guess(board, row, col): Checks the result of a guess on the given board at the specified row and column.
* update_board(board, row, col, result): Updates the given board based on the result of a guess at the specified row and column.
* computer_guess(board): Generates a random guess for the computer on the given board.
* read_scores_from_sheet(): Reads the game scores from a Google Sheet.
* write_score_to_sheet(name, age, score): Writes the player's name, age, and score to a Google Sheet.
* print_board(board): Prints the given board in a human-readable format.
* print_boards(player_board, computer_board, name): Prints the player and computer boards side by side.
* print_scoreboard(): Prints the top 10 players in right order




---