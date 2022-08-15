import signal
import RPi.GPIO as gpio


class Buttons:
    def __init__(self):
        self._pins = [5, 6, 16, 24]
        self.A = "A"
        self.B = "B"
        self.X = "X"
        self.Y = "Y"
        self._labels = [self.A, self.B, self.X, self.Y]
        self._register = {}

        gpio.setmode(gpio.BCM)
        gpio.setup(self._pins, gpio.IN, pull_up_down=gpio.PUD_UP)

        for pin in self._pins:
            # bouncetime is in millis
            gpio.add_event_detect(pin, gpio.FALLING, self.handle_button, bouncetime=100)

    def handle_button(self, pin):
        label = self._labels[self._pins.index(pin)]
        if label not in self._register.keys():
            return
        if self._register[label] is None:
            return
        self._register[label]()

    def register_button(self, label, fn):
        # TODO invalid label?
        self._register[label] = fn


if __name__ == "__main__":
    b = Buttons()
    print("press buttons. Ctrl+C to interrupt")
    signal.pause()
