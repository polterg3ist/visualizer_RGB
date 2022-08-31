import pygame


class Color:
    def __init__(self, screen, rgb: list) -> None:
        self.screen = screen
        self.rgb = rgb
        self.red = rgb[0]
        self.green = rgb[1]
        self.blue = rgb[2]
        self.red_up = False
        self.red_down = False
        self.green_up = False
        self.green_down = False
        self.blue_up = False
        self.blue_down = False
        self.color_surf = pygame.Surface((300, 300))
        self.color_change_value = 1

    def output(self):
        self.screen.blit(self.color_surf, (200, 320))
        self.color_surf.fill((self.red, self.green, self.blue))

    def update(self):
        self.rgb = [self.red, self.green, self.blue]
        if self.red_up:
            if self.red + self.color_change_value > 255:
                self.red = 255
            else:
                self.red += self.color_change_value
        elif self.red_down:
            if self.red - self.color_change_value < 0:
                self.red = 0
            else:
                self.red -= self.color_change_value

        if self.green_up:
            if self.green + self.color_change_value > 255:
                self.green = 255
            else:
                self.green += self.color_change_value
        elif self.green_down:
            if self.green - self.color_change_value < 0:
                self.green = 0
            else:
                self.green -= self.color_change_value

        if self.blue_up:
            if self.blue + self.color_change_value > 255:
                self.blue = 255
            else:
                self.blue += self.color_change_value
        elif self.blue_down:
            if self.blue - self.color_change_value < 0:
                self.blue = 0
            else:
                self.blue -= self.color_change_value
