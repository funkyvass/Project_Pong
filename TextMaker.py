import pygame

# Initialize Pygame
pygame.font.init()

def write(screen, text, font_size, color, position):
    font = pygame.font.Font("Materijali/8-bit-pusab.ttf", font_size)

    # Split the text into lines
    lines = text.split("\n")

    # Calculate the maximum width of the lines to center horizontally
    max_width = max([font.size(line)[0] for line in lines])

    # Calculate the X position to center the text
    x_offset = (screen.get_width() - max_width) // 2

    # Set starting Y position for the first line
    y_offset = position[1]

    # Loop through each line and render it
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x_offset, y_offset)  # Positioning each line

        screen.blit(text_surface, text_rect)

        # Increase the Y offset for the next line
        y_offset += font_size + 5  # Add a little extra space between lines
