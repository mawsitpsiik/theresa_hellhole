import board
import digitalio
import time
import neopixel
y = 0

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)
#pixels[y % 10] = (0, 255, 0)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ButtB = digitalio.DigitalInOut(board.BUTTON_B)
ButtB.direction = digitalio.Direction.INPUT
ButtB.pull = digitalio.Pull.DOWN

ButtA = digitalio.DigitalInOut(board.BUTTON_A)
ButtA.direction = digitalio.Direction.INPUT
ButtA.pull = digitalio.Pull.DOWN

while True:
    if ButtA.value == True:
        y = y + 1
        time.sleep(0.2)
    if ButtB.value == True:
        y = y - 1
        time.sleep(0.2)
    pixels[(y + 1) % 10] = (255, 0, 0)
    pixels[(y + 4) % 10] = (128, 128, 0)
    pixels[(y + 8) % 10] = (0, 0, 255)

    pixels.show()
    pixels.fill(0)


#a


