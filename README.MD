# Tic-Tac-Toe Game with AI Players

## Overview
This project is a command-line-based Tic-Tac-Toe game implemented in Python. The game can be played between two human players or against an "AI" (USED THE AI TERM FOR THE HYPE haha). The AI has two difficulty levels: a "Dumb" player that makes random moves, and an "Impossible" player that uses the Minimax algorithm to play optimally.

Created as a personal project, this game serves as a showcase of my skills in Python. The project was inspired by concepts learned in my economics classes, particularly in Game Theory and Mathematical Economics. Additionally, I developed this code as an "assignment" for the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu. This project represents my personal interpretation and application of the concepts learned, with most of the work being original.

## Features
- Play against another human or against an AI.
- Two AI difficulty levels: "Dumb" (random moves) and "Impossible" (Minimax algorithm).
- Detection of win or draw conditions.

## Project Structure
- `tictactoe.py`: Main class for managing the game, including the game loop, player turns, and board state.
- `ai_players.py`: Contains the `AIPlayer` base class and the specific AI implementations:
  - `DumbPlayer`: An `AI` that selects random valid moves.
  - `MiniMaxPlayer`: An `AI` that uses the Minimax algorithm to make optimal moves.

## Dependencies
This project is implemented purely in Python and relies on standard libraries. No external packages are required.
