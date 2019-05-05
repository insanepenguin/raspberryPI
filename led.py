from gpiozero import LED,Button
from time import sleep

led = LED(17)
button = Button(27)

while True:
	button.when_pressed = led.on
	button.when_released = led.off



