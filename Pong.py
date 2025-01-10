import pygame, sys
from pygame import MOUSEBUTTONDOWN

from TextMaker import write
from button import Button
import TextMaker

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Materijali/8-bit-pusab.ttf", size)


def Play():
    SCREEN.fill(BLACK)
    pygame.display.set_caption("Play")
    BACK_BT = Button(pos=(100, 50), text_input="Back", font=get_font(30),
                     base_color=WHITE, hovering_color=GREEN)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if BACK_BT.checkForInput(MOUSE_POS):
                    MainMenu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        for button in [BACK_BT]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

            pygame.display.update()


def Options():
    SCREEN.fill(BLACK)
    pygame.display.set_caption("Play")
    BACK_BT = Button(pos=(100, 50), text_input="Back", font=get_font(30),
                     base_color=WHITE, hovering_color=GREEN)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if BACK_BT.checkForInput(MOUSE_POS):
                    MainMenu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        for button in [BACK_BT]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

            pygame.display.update()


def About():
    SCREEN.fill(BLACK)
    pygame.display.set_caption("About")
    pygame.display.update()
    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if BACK_BT.checkForInput(MOUSE_POS):
                    MainMenu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        text = """                    Welcome to our version of the classic retro game Pong!\n
                    \n
                    We've taken the timeless game and added a few exciting new features to make it even more fun and challenging.\n
                    Our goal was to capture the spirit of the original while making it a more dynamic experience for everyone to enjoy.\n
                    Both of us, Vasil Panchovski and Simon Ilikj, are students at FINKI (Faculty of Computer Science and Engineering) in Skopje.\n
                    We made this game as part of the course Programming Video Games, where we had the opportunity to dive deep into the world of game development.\n
                    This project allowed us to bring our love for video games to life and put our skills to the test.\n
                    We’ve been passionate about video games for as long as we can remember, and it’s this love that drove us to work on this project.\n
                    We both believe that video games are not just a source of entertainment but also a great way to learn and improve our skills.\n
                    This project has been an amazing journey for us.\n
                    It’s not just about making a game - it’s about taking something we love, adding our personal touch, and sharing it with you.\n
                    We hope you can feel the excitement we had while creating this and that you enjoy playing as much as we loved building it.\n
                
                    Thank you for checking it out! If you love video games as much as we do, we hope this brings you some nostalgia and fun.\n"""

        write(SCREEN, text, 13, WHITE, (100, 300))

        BACK_BT = Button(pos=(100, 50), text_input="Back", font=get_font(30),
                         base_color=WHITE, hovering_color=GREEN)

        for button in [BACK_BT]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

            pygame.display.update()


def MainMenu():
    pygame.display.set_caption('Menu')
    while (True):
        SCREEN.fill(BLACK)

        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BT = Button(pos=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) - 300), text_input="Play", font=get_font(75),
                         base_color=WHITE, hovering_color=GREEN)

        OPTIONS_BT = Button(pos=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)), text_input="Options", font=get_font(75),
                            base_color=WHITE, hovering_color=MAGENTA)

        ABOUT_BT = Button(pos=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + 300), text_input="About", font=get_font(75),
                          base_color=WHITE, hovering_color=CYAN)

        QUIT_BT = Button(pos=(100, 50), text_input="QUIT", font=get_font(30),
                         base_color=WHITE, hovering_color=RED)

        for button in [PLAY_BT, OPTIONS_BT, ABOUT_BT, QUIT_BT]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BT.checkForInput(MOUSE_POS):
                    Play()
                elif OPTIONS_BT.checkForInput(MOUSE_POS):
                    Options()
                elif ABOUT_BT.checkForInput(MOUSE_POS):
                    About()
                elif QUIT_BT.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


MainMenu()

pygame.quit()
