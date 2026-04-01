# 🎮 Tic-Tac-Toe

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame)
![License](https://img.shields.io/badge/license-open--source-lightgrey)

A collection of Tic-Tac-Toe implementations in Python, ranging from a simple two-player CLI game to a fully graphical version with an unbeatable AI.

---

## 📁 Project Structure

```
Tic-Tac-Toe/
├── Tic Tac Toe without AI.py    # Two-player CLI game
├── Tic Tac Toe with AI.py       # Player vs rule-based AI (CLI)
├── Tic_Tac_Toe_Enhanced.py      # Graphical game with Pygame
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** — [Download here](https://www.python.org/downloads/)
- **Pygame** (only for the graphical version)

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🕹️ Versions

### 1. `Tic Tac Toe without AI.py` — Two-Player CLI

A straightforward command-line game for two human players.

- Players take turns entering a number (1–9) to place their mark on the board.
- Detects wins (rows, columns, diagonals) and draws.

**How to run:**
```bash
python "Tic Tac Toe without AI.py"
```

---

### 2. `Tic Tac Toe with AI.py` — Player vs Rule-Based AI (CLI)

A command-line game where a human plays as **X** against a rule-based AI playing as **O**.

- The AI uses a hard-coded strategy: it blocks the player's winning moves, then fills the first available cell.
- Detects wins and draws.

**How to run:**
```bash
python "Tic Tac Toe with AI.py"
```

---

### 3. `Tic_Tac_Toe_Enhanced.py` — Graphical Version with Pygame

A fully graphical Tic-Tac-Toe game built with [Pygame](https://www.pygame.org/).

**Features:**
- Animated X and O symbols drawn on a coloured grid.
- **Menu screen** to choose the game mode.
- **Player vs Player** mode.
- **Player vs AI** mode with two difficulty levels:
  - *Easy* — AI makes random moves.
  - *Hard* — AI uses the **minimax algorithm** (unbeatable).
- Highlighted winning line at end of game.
- Persistent score counter across rounds.
- *Play Again* and *Main Menu* buttons.

**How to run:**
```bash
python Tic_Tac_Toe_Enhanced.py
```

---

## 🗺️ Board Layout

Positions are numbered 1–9, left to right, top to bottom:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

---

## 📦 Requirements

| Version       | Python | External libraries |
|---------------|--------|--------------------|
| Without AI    | 3.x    | None               |
| With AI       | 3.x    | None               |
| Enhanced      | 3.x    | `pygame >= 2.0`    |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repository and open a pull request.

---

## 📄 License

This project is open source. Feel free to use and modify it.

