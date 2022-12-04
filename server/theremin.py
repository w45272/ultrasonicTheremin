import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23 
GPIO_ECHO = 24
triggerPIN = 18
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(triggerPIN, GPIO.OUT)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.1)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    # print(distance)
    return distance

if __name__ == '__main__':
    buzzer = GPIO.PWM(triggerPIN, 440) # Set frequency to 1 Khz
    buzzer.start(10)

    try:
        while True:
            dist = distance()
            print(dist)
            buzzer.ChangeFrequency(dist*10)

    except KeyboardInterrupt:
       GPIO.cleanup()
