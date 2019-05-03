from gpiozero import Button , LED
import down

buttont1 = Button(23)
buttont2 = Button(24)
buttonb1 = Button(13)
ledyellow = LED(17)

while True:
<<<<<<< HEAD
    buttont1.wait_for_press = down.dwn()
    buttont2.wait_for_press = ledyellow.on
    buttont2.wait_for_release = ledyellow.off
    buttonb1.wait_for_press = down.newmeth()
=======
    if buttont1.is_pressed:
        print("One")
    elif buttont2.is_pressed:
        print("Two")
        down.newmeth()
    elif buttonb1.is_pressed and buttont1.is_pressed:
        print("Three")
        down.dwn()
>>>>>>> raspberryPI/master
