# Sudoku - A Python Implementation

This project implements a Sudoku solver in Python. It provides functionalities to play and solve Sudoku puzzles.

## Getting Started
This project requires Python 3 to run.

## How to Play
* Run the script: python sudoku.py
The script will display the initial game board and a corresponding position board that maps numbers to their position on the board.

* Enter the number corresponding to the cell you want to modify.

* Enter the value you want to update the board with. The script will validate your input to ensure it follows the rules of Sudoku. The script will update the board and display the updated board along with the position board.

* The game continues until you choose to stop.

## Rules
The game follows the standard rules of Sudoku.

* You can only enter values between 1 and 4.
* A value cannot be placed in the same row, column, or 2x2 subgrid where it already exists.

## Functionalities
This script currently offers basic functionalities to play Sudoku. 
Here are some possible future functionalities:

* Difficulty Levels: Implement different difficulty levels by pre-populating the board with varying numbers of cells.
* Auto-solve: Add an option for the script to automatically solve the Sudoku puzzle.
* Error Handling: Improve error handling to provide more informative messages for invalid user input.
* Auto Board Building: Automate and randomize the process of building a board
* Win or Lose: Create a competitive standard to determine win or lose