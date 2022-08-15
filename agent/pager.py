from buttons import Buttons
from display import Display
import signal
from speaker import Speaker
import time


class Pager:
    def __init__(self):
        self._display = Display()
        self._speaker = Speaker()
        self._buttons = Buttons()
        self._display.clear()

        self._display.message("booting...")

        self._buttons.register_button(self._buttons.X, self._display_image)
        self._buttons.register_button(self._buttons.Y, self._display_message)
        self._buttons.register_button(self._buttons.A, self._play_sound)

        time.sleep(0.5)

        self._display.clear()

    def _display_image(self):
        self._display.cover_with_image("IMG_5292.jpeg")
        time.sleep(2)
        self._display.clear()

    def _display_message(self):
        self._display.message()
        time.sleep(2)
        self._display.clear()

    def _play_sound(self):
        self._speaker.play_clip("7.wav")
        time.sleep(2)
        self._display.clear()


if __name__ == "__main__":
    p = Pager()
    print("pager is running. Ctrl+C to stop")
    signal.pause()
