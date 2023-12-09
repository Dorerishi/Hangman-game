import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.Font(None, 36)

user_input = ""

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace
                    user_input = user_input[:-1]
                elif event.unicode.isprintable():
                    # Handle printable characters
                    user_input += event.unicode

        screen.fill(white)

        text_surface = font.render("Input: " + user_input, True, black)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
