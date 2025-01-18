import pygame

# Initialize Pygame
pygame.font.init()

def write(screen, text, font_size, color, position):
    font = pygame.font.Font("Materijali/8-bit-hud.ttf", font_size)

    rendered_text = font.render(text, True, color)


    text_rect = rendered_text.get_rect()


    text_rect.center = position


    screen.blit(rendered_text, text_rect.topleft)
