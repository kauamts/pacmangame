#!/bin/bash

# PacMan Game Launcher Script for Mac
echo "🟡 Starting PacMan Game..."
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first:"
    echo "   brew install python3"
    echo "   or download from https://www.python.org/downloads/"
    exit 1
fi

# Check if pygame is installed
python3 -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "🎮 Installing pygame..."
    pip3 install pygame || {
        echo "❌ Failed to install pygame. Try manually:"
        echo "   pip3 install pygame"
        exit 1
    }
fi

# Run the game
echo "🚀 Launching PacMan..."
python3 pacman_game.py

echo ""
echo "👋 Thanks for playing PacMan!"