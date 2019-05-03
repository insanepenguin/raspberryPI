from gpiozero import Button , LED
import down

buttont1 = Button(23)
buttont2 = Button(24)
buttonb1 = Button(13)
ledyellow = LED(17)

while True:
    buttont1.wait_for_press = down.dwn
    buttont2.wait_for_press = ledyellow.on
    buttont2.wait_for_released = ledyellow.off
    buttonb1.wait_for_press = down.newmeth
