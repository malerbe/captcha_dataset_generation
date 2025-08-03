import os
import secrets
from PIL.ImageFont import FreeTypeFont, truetype
from PIL.Image import new as createImage, Image, Transform, Resampling
from PIL.ImageDraw import Draw, ImageDraw


DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
print(DATA_DIR)

DEFAULT_FONTS = [os.path.join(DATA_DIR, 'Quicksand_Book.ttf')]

def random_color(
        start,
        end,
        opacity = None):
    red = secrets.randbelow(end - start + 1) + start
    green = secrets.randbelow(end - start + 1) + start
    blue = secrets.randbelow(end - start + 1) + start
    if opacity is None:
        return red, green, blue
    return red, green, blue, opacity

class ImageCaptcha:
    def __init__(
            self,
            width = 160,
            height = 60,
            fonts = None,
            font_sizes = [48, 50, 52]):
        
        self._width = width
        self._height = height
        self._fonts = fonts or DEFAULT_FONTS
        self._font_sizes = font_sizes

    def create_captcha_image(self, chars, foreground_color, background_color):
        image = createImage('RGB', (self._width, self._height), background_color)
        draw = Draw(image)

        images: []
        for c in chars:
            if secrets.randbits(32) / (2**32) > self.word_space_probability:
                images.append(self._draw_character(" ", draw, color))
            images.append(self._draw_character(c, draw, color))


    def generate_image(self, chars, background_color, foreground_color):
        background_color = background_color if background_color else random_color(200, 255)
        foreground_color = foreground_color if foreground_color else random_color(10, 200, secrets.randbelow(36) + 220)

        image = self.create_captcha_image(chars, foreground_color, background_color)

        print(background_color, foreground_color)

    



if __name__ == "__main__":
    test = ImageCaptcha()
    test.generate_image('test', None, None)