import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)		#trigger pin
GPIO.setup(10, GPIO.IN)		#echo pin
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12,100)
dc = 0

def distance():
    # set Trigger to HIGH
    GPIO.output(8, GPIO.HIGH)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(8, GPIO.LOW)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(10) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(10) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
    
try:
    while True:
        d = distance()
        print(d)
        pwm.start(dc)
        if d<=12.5 and d>0:
            pwm.ChangeDutyCycle((12.5-d)*8)
 
# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
