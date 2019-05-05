from gpiozero import Button , LED
import down

buttont1 = Button(23)
buttonb1 = Button(26)
ledyellow = LED(17)
ledgreen = LED(6)
while True:
    buttont1.when_pressed = down.dwn()
    buttont1.when_released = ledyellow.on
    buttonb1.when_pressed = down.startServer()
    buttonb1.when_released = ledgreen.on



