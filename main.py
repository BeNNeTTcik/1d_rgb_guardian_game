# main.py
import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 60
LED_PIN = 18          # typowo PWM0 (GPIO18) dla rpi-ws281x
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 64
LED_INVERT = False
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

pos = 0
direction = 1

while True:
    # prosta animacja: “strażnik” jeździ tam i z powrotem
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.setPixelColor(pos, Color(0, 255, 0))
    strip.show()

    pos += direction
    if pos <= 0 or pos >= LED_COUNT - 1:
        direction *= -1

    time.sleep(1/60)  # tick 60 Hz
