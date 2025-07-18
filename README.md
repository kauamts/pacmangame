# PacMan Game

A classic PacMan-style game built with Python and Pygame that runs on Mac (and other platforms).

## Features

- **Classic Gameplay**: Navigate through a maze, collect dots, and avoid ghosts
- **Power Pellets**: Eat power pellets to turn ghosts scared and eat them for bonus points
- **Smart Ghost AI**: Ghosts chase the player and move randomly when scared
- **Score System**: Earn points for collecting dots (10 pts), power pellets (50 pts), and eating ghosts (200 pts)
- **Lives System**: Start with 3 lives, lose one when caught by a ghost
- **Victory Condition**: Collect all dots to win the level
- **Screen Wrapping**: Move through the left/right edges of the screen
- **Smooth Controls**: Responsive keyboard controls with WASD or arrow keys

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Mac Installation

1. **Install Python** (if not already installed):
   ```bash
   # Using Homebrew (recommended)
   brew install python3
   
   # Or download from https://www.python.org/downloads/
   ```

2. **Clone or download this repository**:
   ```bash
   git clone <repository-url>
   cd pacman-game
   ```

3. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

   Or install pygame directly:
   ```bash
   pip3 install pygame
   ```

## How to Run

### Method 1: Direct Python Execution
```bash
python3 pacman_game.py
```

### Method 2: Using the Launch Script
```bash
./run_game.sh
```

### Method 3: Mac App Bundle (Recommended for Mac)
1. Create the Mac app bundle:
   ```bash
   python3 create_mac_app.py
   ```
2. Double-click `PacMan.app` in Finder to launch the game
3. The app will feel like a native Mac application!

## Controls

- **Arrow Keys** or **WASD**: Move PacMan up, down, left, right
- **R**: Restart game (when game over or victory)
- **Close Window** or **Escape**: Quit game

## Gameplay

1. **Objective**: Collect all the white dots in the maze while avoiding the colored ghosts
2. **Movement**: Use arrow keys or WASD to navigate through the maze
3. **Dots**: Small white dots give you 10 points each
4. **Power Pellets**: Large white dots (in corners) give you 50 points and make ghosts scared (blue) for 10 seconds
5. **Eating Ghosts**: While ghosts are scared, you can eat them for 200 points each
6. **Lives**: You start with 3 lives. Touching a non-scared ghost costs you a life
7. **Victory**: Collect all dots to complete the level
8. **Game Over**: Lose all 3 lives and the game ends

## Game Elements

- **Yellow Circle**: PacMan (player)
- **Blue Rectangles**: Maze walls
- **Small White Dots**: Regular dots (10 points)
- **Large White Dots**: Power pellets (50 points)
- **Colored Ghosts**: 
  - Red Ghost: Aggressive chaser
  - Pink Ghost: Ambush style
  - Cyan Ghost: Patrol style  
  - Orange Ghost: Random movement
- **Blue Ghosts**: Scared state (can be eaten)

## Troubleshooting

### Common Issues on Mac

1. **"pygame not found" error**:
   ```bash
   pip3 install --upgrade pip
   pip3 install pygame
   ```

2. **Permission issues**:
   ```bash
   pip3 install --user pygame
   ```

3. **Python version issues**:
   Make sure you're using Python 3.7+:
   ```bash
   python3 --version
   ```

4. **Display issues on macOS**:
   If you encounter display problems, try:
   ```bash
   export SDL_VIDEODRIVER=metal
   python3 pacman_game.py
   ```

### Performance Tips

- Close other applications to improve game performance
- Ensure your Mac meets minimum requirements (any Mac from the last 10 years should work fine)
- The game runs at 60 FPS for smooth gameplay

## System Requirements

- **macOS**: 10.9 or later
- **RAM**: 512 MB minimum
- **Display**: Any resolution (game window is 800x600)
- **Python**: 3.7 or higher

## Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes!

## License

This project is open source. See the LICENSE file for details.

---

Enjoy playing PacMan! 🟡👻