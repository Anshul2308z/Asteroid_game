import pygame
from constants import *
def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__": #This line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module.
    main()
