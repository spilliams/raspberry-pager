from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from ST7789 import ST7789
import sys
import time


class Display:
    def __init__(self):
        self._original_backlight = 13
        try:
            self.set_font("/usr/share/fonts/truetype/range-mono/range-mono-regular.ttf")
        except FileNotFoundError:
            self.set_font()

        self._st7789 = ST7789(
            rotation=90,  # Needed to display the right way up on Pirate Audio
            port=0,  # SPI port
            cs=1,  # SPI port Chip-select channel
            dc=9,  # BCM pin used for data/command
            backlight=self._original_backlight,
            spi_speed_hz=80 * 1000 * 1000,
        )
        self._st7789.begin()

    def set_font(self, filename="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        p = Path(filename)
        if not p.is_file():
            print(f"Font {filename} does not exist or is not a file.", file=sys.stderr)
            raise FileNotFoundError
        self._font = filename

    def clear(self):
        width = self._st7789.width
        height = self._st7789.height

        image = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 240, 240), (0, 0, 0))
        self._st7789.display(image)

    def turn_off(self):
        self.clear()
        self._st7789.set_backlight(0)

    def turn_on(self):
        self.clear()
        self._st7789.set_backlight(self._original_backlight)

    def cover_with_image(self, filename):
        width = self._st7789.width
        height = self._st7789.height
        image = Image.open(filename)
        image = image.resize((width, height))
        self._st7789.display(image)

    def message(self, message="Hello, world!"):
        width = self._st7789.width
        height = self._st7789.height
        img = Image.new("RGB", (width, height), color=(0, 0, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self._font, 30)

        size_x, size_y = draw.textsize(message, font)
        text_x = (width - size_x) // 2
        text_y = (height - size_y) // 2

        draw.rectangle((0, 0, width, height), (0, 0, 0))
        draw.text((text_x, text_y), message, font=font, fill=(255, 255, 255))
        self._st7789.display(img)


def main():
    d = Display()
    d.clear()
    d.cover_with_image("IMG_5292.jpeg")
    time.sleep(2.0)
    d.message()
    time.sleep(2.0)
    d.clear()


if __name__ == "__main__":
    main()
