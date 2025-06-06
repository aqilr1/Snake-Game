# 🐍 Snake Game - Python Turtle

This is a simple implementation of the classic Snake game using Python's `turtle` graphics module. 

---

## 🎮 Game Features

- Snake movement controlled using **WASD** keys
- Food spawns randomly on the screen
- Score increases on food consumption
- Collision detection:
  - With walls → game over
  - With tail → game over
- Clean scoreboard with live updates

---

## 📁 Project Structure

snake_game:

- main.py # Main game loop and event handling
- snake.py # Snake class and movement logic
- food.py # Food class with random spawn logic
- scoreboard.py # ScoreBoard class to display score and game over

## 🧠 Concepts Practiced

- Object-Oriented Programming (OOP)
- Inheritance and Encapsulation
- Event-driven programming with keyboard listeners
- Modular code organization
- GUI programming with the `turtle` module
- Basic game development logic

---

## ▶️ How to Run
python main.py

A game window will open. Use W, A, S, D keys to control the snake.

### Prerequisites

Make sure you have Python installed. This game uses only built-in libraries (`turtle`, `random`, `time`).
