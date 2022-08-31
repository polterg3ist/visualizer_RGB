import requests
from bs4 import BeautifulSoup


def get_colors_list() -> list:
    colors = []
    with open("colors_base.txt", 'r') as file:
        lines = file.readlines()

        for line in lines:
            colorNameAndRgb = line.split("| ")
            color_name = colorNameAndRgb[0]
            rgb_red = colorNameAndRgb[1]
            rgb_green = colorNameAndRgb[2]
            rgb_blue = colorNameAndRgb[3][:-1]
            colors.append([color_name, rgb_red, rgb_green, rgb_blue])

        return colors


def parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    return soup.find_all('tr')


def main():
    url = "https://colorscheme.ru/color-names.html"
    tr = parse(url)
    tr.pop(0)
    colors = []
    for tag in tr:
        info = tag.find_all('td')
        color_name = str(info[1])[4:-5]
        color_red = str(info[3])[4:-5]
        color_green = str(info[4])[4:-5]
        color_blue = str(info[5])[4:-5]
        colors.append([color_name, color_red, color_green, color_blue])
        print(f"COLOR {color_name} RED {color_red} GREEN {color_green} BLUE {color_blue}")

    with open("colors_base.txt", 'w') as file:
        for color in colors:
            file.write(f"{color[0]}| {color[1]}| {color[2]}| {color[3]}\n")


if __name__ == '__main__':
    main()