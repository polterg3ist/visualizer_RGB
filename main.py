import pygame
import controls
from color import Color
from text import Text
from color_name import ColorName


def main():
    pygame.init()
    FPS = 30
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 720))
    pygame.display.set_caption("Colorizer")
    color = Color(screen, [255, 255, 255])
    clr_name = ColorName(color)
    text = Text(screen, color, clr_name)

    while True:
        clock.tick(FPS)
        controls.events(color)
        controls.update(screen, color, text, clr_name)


if __name__ == "__main__":
    main()
