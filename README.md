Snake Game 🐍

This is a simple implementation of the classic Snake game using Python's Turtle graphics library. The player controls a snake to eat food that appears randomly on the screen. Each time the snake eats food, it grows in length, and the player's score increases. The game ends if the snake collides with the wall or itself.

Features

Simple and fun gameplay - Control the snake using the arrow keys to eat food and grow longer.
Scoring system - Keep track of the score with a scoreboard that updates in real time.
Game Over Detection - The game ends when the snake hits a wall or collides with itself.
Installation

To run this game, you need Python installed on your machine.

Clone this repository:
git clone https://github.com/your-username/snake-game.git
Navigate to the project directory:
cd snake-game
Ensure you have the Turtle graphics library installed (it's included with Python by default).
Run the game:
python main.py
How to Play

Use the Up, Down, Left, and Right arrow keys to control the snake's direction.
Guide the snake to the food. Each time the snake eats food, it grows in length, and your score increases.
Avoid hitting the walls or the snake's own body. If this happens, the game will end.
File Structure

main.py: The main file that runs the game loop.
snake.py: Contains the Snake class, responsible for creating and moving the snake.
food.py: Contains the Food class, responsible for generating food at random locations.
scoreboard.py: Contains the ScoreBoard class, which keeps track of and displays the score.
Gameplay

Start the game and move the snake using arrow keys.
Eat the food to grow the snake and increase your score.
Avoid collisions with the wall or the snake's tail.
Code Overview

main.py
This file initializes the game screen, listens for key presses, and runs the main game loop. It includes logic for detecting collisions with the wall, food, and tail.

snake.py
Defines the Snake class. Handles the movement of the snake and the functionality to grow the snake when food is eaten.

food.py
Defines the Food class. Randomly generates food on the screen and refreshes it each time it’s eaten by the snake.

scoreboard.py
Defines the ScoreBoard class. Manages and displays the current score on the screen and shows a "Game Over" message if the snake dies.

Example Gameplay

Future Enhancements

High score: Add functionality to save the highest score achieved.
Pause/Resume: Allow the player to pause and resume the game.
Levels: Increase speed as the snake gets longer.
License

This project is open-source and available under the MIT License.
