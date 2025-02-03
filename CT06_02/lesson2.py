import os
import random
import time
import sys

# Screen size
WIDTH = 20
HEIGHT = 10

# Pac-Man and Ghost setup
pacman_pos = [5, 5]  # Starting position of Pac-Man
ghost_pos = [random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1)]
dots = [(random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1)) for _ in range(5)]

# Initialize game status
score = 0
game_over = False

def print_screen():
    """Clear the screen and print the current game state."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] == pacman_pos:
                print('P', end='')  # Print Pac-Man
            elif [x, y] == ghost_pos:
                print('G', end='')  # Print Ghost
            elif (x, y) in dots:
                print('.', end='')  # Print Dot
            else:
                print(' ', end='')  # Empty space
        print()
    print(f"Score: {score}")

def move_pacman(direction):
    """Move Pac-Man based on the direction."""
    global pacman_pos
    if direction == 'w' and pacman_pos[1] > 0:  # Move up
        pacman_pos[1] -= 1
    elif direction == 's' and pacman_pos[1] < HEIGHT - 1:  # Move down
        pacman_pos[1] += 1
    elif direction == 'a' and pacman_pos[0] > 0:  # Move left
        pacman_pos[0] -= 1
    elif direction == 'd' and pacman_pos[0] < WIDTH - 1:  # Move right
        pacman_pos[0] += 1

def check_collision():
    """Check if Pac-Man eats a dot or collides with a ghost."""
    global score, game_over, dots
    if tuple(pacman_pos) in dots:
        score += 10
        dots.remove(tuple(pacman_pos))
    if pacman_pos == ghost_pos:
        game_over = True

def move_ghost():
    """Move the ghost randomly."""
    global ghost_pos
    ghost_pos[0] += random.choice([-1, 1])
    ghost_pos
