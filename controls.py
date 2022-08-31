import pygame
from sys import exit as close_game


def events(color):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                color.red_up = True
            elif event.key == pygame.K_a:
                color.red_down = True

            if event.key == pygame.K_w:
                color.green_up = True
            elif event.key == pygame.K_s:
                color.green_down = True

            if event.key == pygame.K_e:
                color.blue_up = True
            elif event.key == pygame.K_d:
                color.blue_down = True

            if event.key == pygame.K_UP:
                color.color_change_value += 1
            elif event.key == pygame.K_DOWN:
                if color.color_change_value > 1:
                    color.color_change_value -= 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                color.red_up = False
            elif event.key == pygame.K_a:
                color.red_down = False

            if event.key == pygame.K_w:
                color.green_up = False
            elif event.key == pygame.K_s:
                color.green_down = False

            if event.key == pygame.K_e:
                color.blue_up = False
            elif event.key == pygame.K_d:
                color.blue_down = False


def update(screen, color, text, color_name):
    # screen.fill((255, 200, 150))    # background 1 (body skin)
    screen.fill((0, 0, 0))            # background 2 (full black)
    color.output()
    color.update()
    text.output()
    text.update()
    color_name.compare()
    pygame.display.flip()
