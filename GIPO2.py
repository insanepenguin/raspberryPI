import RPi.GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(13,GPIO.IN)
while True:
    if GPIO.input(23):
        print('Input was HIGH')
        GPIO.output(17,True)
    else:
        print('Input was LOW')
        GPIO.output(17, False)