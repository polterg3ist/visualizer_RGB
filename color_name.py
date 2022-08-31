from rgb_color_name.color_parse_rgb import get_colors_list


class ColorName:
    def __init__(self, clr_obj):
        self.clr_obj = clr_obj
        self.colors = get_colors_list()
        self.name = None

    def compare(self):
        for clr in self.colors:
            print(f"search in {clr}")
            near_red = [self.clr_obj.red + near for near in range(-5, 6) if -1 < self.clr_obj.red + near < 256]
            near_green = [self.clr_obj.green + near for near in range(-5, 6) if -1 < self.clr_obj.green + near < 256]
            near_blue = [self.clr_obj.blue + near for near in range(-5, 6) if -1 < self.clr_obj.green + near < 256]
            if int(clr[1]) in near_red and int(clr[2]) in near_green and int(clr[3]) in near_blue:
                print(f"color found {clr[0]}")
                self.name = clr[0]
                break
            self.name = "Названия для этого цвета не существует"
