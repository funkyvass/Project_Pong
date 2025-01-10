import random

import pygame, sys
from pygame import MOUSEBUTTONDOWN, KEYDOWN

from TextMaker import write
from button import Button
import TextMaker

pygame.init()
clock = pygame.time.Clock()
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
CENTERx = SCREEN_WIDTH / 2
CENTERy = SCREEN_HEIGHT / 2
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# GAME ELEMENTS
#BALL
ball_size = 50
ball_radius = 10
ball_speedx = 14
ball_speedy = 14
#PLAYER
paddle_height = 140
player_speed = 0
opponent_speed = 15
ai_fear_factor = 50
def get_font(size):
    return pygame.font.Font("Materijali/8-bit-pusab.ttf", size)



def Game_Logic():
    global player_speed
    ball = pygame.Rect(CENTERx - ball_size/2, CENTERy - ball_size/2, ball_size, ball_size)
    player1 = pygame.Rect(SCREEN_WIDTH - 20, CENTERy - paddle_height/2, 10, paddle_height )
    player2 = pygame.Rect(10, CENTERy - paddle_height / 2, 10, paddle_height)

    def ballrestart():
        global ball_speedx, ball_speedy
        ball.center = (CENTERx - ball_size / 2, CENTERy - ball_size / 2)
        ball_speedx *= random.choice((1, -1))
        ball_speedy *= random.choice((1, -1))

    
    def ball_animation():
        global ball_speedx, ball_speedy
        ball.x += ball_speedx
        ball.y += ball_speedy
        # BOUNCE
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speedy *= -1
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ballrestart()

        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speedx *= -1


    def player1_animation():
        global player_speed
        player1.y += player_speed
        # BOUNCE
        if player1.top <= 0:
            player1.top = 0
        if player1.bottom >= SCREEN_HEIGHT:
            player1.bottom = SCREEN_HEIGHT

    def opponent_ai_animation():
        if player2.centery < ball.y + ai_fear_factor:
            player2.top += opponent_speed
        if player2.centery > ball.y - ai_fear_factor:
            player2.bottom -= opponent_speed

        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= SCREEN_HEIGHT:
            player2.bottom = SCREEN_HEIGHT

    while True:
        SCREEN.fill(BLACK)
        clock.tick(60)
        MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_DOWN:
                    player_speed = 10
                if event.key == pygame.K_UP:
                    player_speed = -10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player_speed = 0

        player1.y += player_speed
        ball_animation()
        player1_animation()
        opponent_ai_animation()


        # DRAW ITEMS
        pygame.draw.circle(SCREEN, WHITE, (ball.x + ball_radius, ball.y + ball_radius), ball_radius)
        pygame.draw.rect(SCREEN, WHITE, player1)
        pygame.draw.rect(SCREEN, WHITE, player2)
        pygame.draw.aaline(SCREEN, GRAY, (CENTERx,0), (CENTERx, SCREEN_HEIGHT))
        pygame.display.flip()






def PlayScreen():
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
                    #PlayScreen()
                    Game_Logic()
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
