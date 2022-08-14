import signal
import RPi.GPIO as gpio


class Buttons:
    def __init__(self):
        self._pins = [5, 6, 16, 24]
        self._labels = ["A", "B", "X", "Y"]

        gpio.setmode(gpio.BCM)
        gpio.setup(self._pins, gpio.IN, pull_up_down=gpio.PUD_UP)

        for pin in self._pins:
            # bouncetime is in millis
            gpio.add_event_detect(pin, gpio.FALLING, self.handle_button, bouncetime=100)

    def handle_button(self, pin):
        i = self._pins.index(pin)
        print(f"Button {self._labels[i]} pressed")


if __name__ == "__main__":
    b = Buttons()
    signal.pause()
