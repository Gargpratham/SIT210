# including the required libraries
from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # setting the gpio mode to BCM

LED = LED(5)            # setting pin 5 as LED pin

win = Tk()  # opening the window
win.title("Morsecode")  # setting window title

# creating dot function to blink the LED for shorter time (0.5 sec on and 0.5 sec off) 
def dot():
    LED.on()
    sleep(0.5)
    LED.off()
    sleep(0.5)

# creating dot function to blink the LED for shorter time (1.5 sec on and 0.5 sec off) 
def dash():
    LED.on()
    sleep(1.5)
    LED.off()
    sleep(0.5)

# defining the morsecode of all the alphabets in a 2D array
MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..'}

inputtxt = StringVar() # variable of string type

# function to fix the characters entry limit to 12 only.
def callback(inputtxt):
    value = inputtxt.get()
    if len(value) > 12: inputtxt.set(value[:12])

# convert funtion to convert the alphabets entered into morsecode (dot and dash)
def morseCode():
    value = inputBox.get()  # taking the user input
    for letter in value:
        for symbol in MORSE[letter.upper()]:
            if symbol == '.':
                dot()
            elif symbol == '-':
                dash()

# function to exit the code execution
def Exit():
    GPIO.cleanup()
    win.destroy()

# label created to display text on GUI
label = Label(win, text='Enter 12 characters to convert to morse code', font=('Arial', 20))
label.pack()


inputtxt.trace('w', lambda name, index, mode, inputxt=inputtxt: callback(inputtxt)) # limiting the number of characters in the text box as per the callback function created above
inputBox = Entry(win, textvariable=inputtxt, width=25, font=('Arial', 40))          # input box created to get the entry of alphabets to convert them to morse code
inputBox.pack()

# Button to execute the code and convert the alphabets to morse code and blink the LED accordingly
printButton = Button(win, bg='pink', font=('Arial', 25), text="RUN", command=morseCode, height=2, width=15)
printButton.pack()

# Button to stop the code and close the GUI window
exitButton = Button(win, text="Exit", font=('Arial', 25), command=Exit, bg="grey", height=1, width=10)
exitButton.pack()

win.mainloop()
