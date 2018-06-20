import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3, 50)
pwm.start(0)

class FishFeeder():
    
    def __init__(self):
        pass

    def SetAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(3, True)
        pwm.ChangeDutyCycle(duty)
        sleep(0.5)
        GPIO.output(3, False)
        pwm.ChangeDutyCycle(0)

    def FeedNow(self, duration, angle):
        FishFeeder().SetAngle(angle)
        sleep(duration)
        FishFeeder().SetAngle(180)
    
    def Cancel(self):
        pwm.stop()
        GPIO.cleanup()