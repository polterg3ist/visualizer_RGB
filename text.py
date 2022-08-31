import pygame


class Text:
    def __init__(self, screen, color_object, color_name_obj):
        self.screen = screen
        self.color_object = color_object
        self.color_change_value = color_object.color_change_value
        self.color_name_obj = color_name_obj
        self.one_percent = sum(self.color_object.rgb) / 100
        self.red_in_percent = self.color_object.red // self.one_percent
        self.green_in_percent = self.color_object.green // self.one_percent
        self.blue_in_percent = self.color_object.blue / self.one_percent

    def update(self):
        self.color_change_value = self.color_object.color_change_value
        self.one_percent = sum(self.color_object.rgb) / 100
        if self.one_percent <= 0:
            self.one_percent = 1
        self.red_in_percent = self.color_object.red / self.one_percent
        self.green_in_percent = self.color_object.green / self.one_percent
        self.blue_in_percent = self.color_object.blue / self.one_percent

    def output(self):
        font1 = pygame.font.SysFont('freesanbold.ttf', 60)
        font2 = pygame.font.SysFont('freesanbold.ttf', 42)

        red_text = f"Red = {self.color_object.red} Total = {self.red_in_percent:.1f}%"
        green_text = f"Green = {self.color_object.green} Total = {self.green_in_percent:.1f}%"
        blue_text = f"Blue = {self.color_object.blue} Total = {self.blue_in_percent:.1f}%"
        ccv_text = f"Speed = {self.color_change_value}"    # ccv = Color Change Value (Bottom text speed changer)
        name_text = f"{self.color_name_obj.name}"

        red = font1.render(red_text, True, (self.color_object.red, 0, 0))
        green = font1.render(green_text, True, (0, self.color_object.green, 0))
        blue = font1.render(blue_text, True, (0, 0, self.color_object.blue))
        ccv = font2.render(ccv_text, True, (80, 130, 80))
        name = font2.render(name_text, True, (66, 49, 137))

        self.screen.blit(red, red.get_rect(center=(350, 25)))
        self.screen.blit(green, green.get_rect(center=(350, 65)))
        self.screen.blit(blue, blue.get_rect(center=(350, 105)))
        self.screen.blit(ccv, ccv.get_rect(center=(350, 670)))
        self.screen.blit(name, name.get_rect(center=(350, 150)))
