import pygame
from config import *
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Game():
    """
    Main Game Class
    Initializes PyGame
    Sets Screen Size
    Sets Game Font
    Sets Game Clock
    Main Game Loop While Running = True
    Contains Game Sprite Sheets
    Method for creating map
    methods for different screens
    method for the actual game play loop playing = True
    add sprites to layered updates
    create the tile map
    method for game events
    method for updating the game sprites
    method for drawing on the screen
    method running the game, call events, update and draw
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.running = True

    def event(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False

                elif event.type == QUIT:
                    running = False


    def draw(self):
        # self.screen.fill(WHITE)
        # surf = pygame.Surface((50,50))
        # surf.fill((0,0,0))
        # rect = surf.get_rect
        pygame.draw.circle(self.screen, BLUE, (250, 250), 75)
        pygame.display.flip()

    def main(self):
        # while self.running():
        self.draw()
        self.event()
        