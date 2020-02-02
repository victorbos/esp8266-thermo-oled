from machine import Pin, I2C
import ssd1306

class Screen:
    def __init__(self):
        i2c = I2C(-1, scl=Pin(5, Pin.OUT), sda=Pin(4, Pin.OUT))
        self._oled = ssd1306.SSD1306_I2C(64, 48, i2c)
        self._lines = [""] * 5

    def reset(self):
        self._oled.fill(0)

    def text(self, msg, line):
        self._lines[line] = msg

    def show(self):
        self.reset()
        for i, line in enumerate(self._lines):
            self._oled.text(line, 0, i * 10, 1)
        self._oled.show()
