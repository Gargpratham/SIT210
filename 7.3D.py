import RPi.GPIO as GPIO     #import RPi GPIO library
import time                 #import time library
GPIO.setwarnings(False)     #used to disable all the warnings
GPIO.setmode(GPIO.BOARD)    #setting the method as board
GPIO.setup(8, GPIO.OUT)		#trigger pin set at pin number 8
GPIO.setup(10, GPIO.IN)		#echo pin set at pin number 10
GPIO.setup(12, GPIO.OUT)    # LED pin set at pin number 12
pwm = GPIO.PWM(12,100)      # variable pwm created and set as the PWM pin at 12 where the LED is connected. The value of PWM goes upto 100.
dc = 0                      # variable dc set as 0

def distance():             # function is defined where distance is calculated of the object from ultrsonic sensor
    # set Trigger to HIGH
    GPIO.output(8, GPIO.HIGH)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(8, GPIO.LOW)
 
    StartTime = time.time() # varibale StartTime set to record start time of the code 
    StopTime = time.time()  # varibale StopTime set to record end time of the code
 
    # save StartTime
    while GPIO.input(10) == 0:  # when GPIO number 10 that is echo pin is at low
        StartTime = time.time() # set to record the start time in seconds
 
    # save time of arrival
    while GPIO.input(10) == 1:  # when GPIO number 10 that is echo pin is at high that means it has received a value after the ultrasoinc wave is bounced back to the sensor.
        StopTime = time.time()  # set to record the end time in seconds
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance     #value of distance is returned
    
try:
    while True:         #while loop to run the main code
        d = distance()  # d varibale is set equal to the distance function to get the distance
        print(d)        # distance is printed
        pwm.start(dc)   # the initial value of PWM is set at dc which is 0. This means initially the LED is at zero brightness
        if d<=12.5 and d>0: # setting the value of distance between 0 and 12.5 to test the system
            pwm.ChangeDutyCycle((12.5-d)*8) # change duty cycle function used to controll the brightness as per the distance of the object from the sensor.
                                            #Suppose d=0, then the cycle becomes 12.5*8=100 that is the LED will be at the highest brightness. 
                                            #As the valuie of d increases, the value of duty cycle decreases and therefore the brightness will decrease
 
# Reset by pressing CTRL + C. Code will stop working
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
