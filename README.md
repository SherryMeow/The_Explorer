
# The Explorer Game

## Overview
**The Explorer** is a text-based adventure game where players navigate through different locations, collect items, and solve puzzles to progress through the game. The game features a dynamic inventory system and multiple paths with unique outcomes. The player’s goal is to explore the game world, interact with objects and characters, and ultimately defeat a dragon to claim victory.

## Table of Contents
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Features](#game-features)
- [Cheat Mode](#cheat-mode)

## Installation

1. Clone the repository:

   ```bash
   git clone <git@github.com:superzta/The_Explorer.git>
   ```

2. Navigate to the project directory:

   ```bash
   cd The_Explorer
   ```

3. Run the game:

   ```bash
   python startgame.py
   ```

## How to Play

- The game starts at the entrance of a castle.
- Navigate by typing commands such as "west", "east", "north", "south", etc.
- You will encounter various locations like the forest, courtyard, village, and others.
- Explore different areas to find items and solve puzzles.
- Use the items in your inventory to overcome obstacles and progress further into the game.
- Pay attention to in-game instructions and clues to figure out the best way to proceed.

### Example Commands:
- **"buy"**: To purchase an item from the market.
- **"explore"**: To explore a location like the forest.
- **"talk"**: To interact with characters like the bartender.
- **"enter"**: To enter a specific location like the castle (if conditions are met).
- **"climb"**: To climb structures like the tower.

## Game Features

- **Inventory Management**: Collect items like gold, a sword, or a map. Keep track of your inventory throughout the game.
- **Dynamic Locations**: Explore multiple unique locations, each with its own challenges and puzzles.
- **Puzzles**: Solve riddles, play games of chance, and outwit enemies.
- **Combat**: Engage in turn-based combat with a dragon, where timing and quick input matter.
- **Cheat Mode**: Start the game with additional items and advantages if desired.

## Cheat Mode

To enable cheat mode, which starts the game with key items like gold, a sword, a key, and more, run the game with the `-c` flag:

```bash
python startgame.py -c
```

This will provide you with:
- 100 Gold
- Sword
- Key
- Lockpick
- Blessing
- Boat Pass