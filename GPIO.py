from gpiozero import Button , LED
import down

buttont1 = Button(23)
buttont2 = Button(24)
buttonb1 = Button(13)
ledyellow = LED(17)

while True:
    if buttont1.is_pressed:
        print("One")
    elif buttont2.is_pressed:
        print("Two")
        down.newmeth()
    elif buttonb1.is_pressed and buttont1.is_pressed:
        print("Three")
        down.dwn()

