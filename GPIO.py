from gpiozero import Button , LED
import down

buttont1 = Button(23)
buttont2 = Button(24)
buttonb1 = Button(13)
ledyellow = LED(17)
x = False
y = False
while True:
    buttont1.when_pressed = ledyellow.on()
    buttont1.when_released = ledyellow.off()
    buttont2.when_pressed = down.newmeth();
    buttont2.when_released = ledyellow.off()
    buttonb1.when_pressed = down.newmeth();
    if(x == True and y == True):
        down.dwn()
    else:
        print("Cont")
