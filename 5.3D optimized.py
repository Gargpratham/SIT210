# including the required libraries
from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # setting the gpio mode to board

LED = LED(5)

win = Tk()  # opening the window
win.title("Morsecode")  # setting window title


def dot():
    LED.on()
    sleep(0.5)
    LED.off()
    sleep(0.5)

def dash():
    LED.on()
    sleep(1.5)
    LED.off()
    sleep(0.5)

# defining the morsecode of all the alphabets
MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..'}

inputtxt = StringVar()

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


def Exit():
    GPIO.cleanup()
    win.destroy()

label = Label(win, text='Enter 12 characters to convert to morse code', font=('Arial', 20))
label.pack()

inputtxt.trace('w', lambda name, index, mode, inputxt=inputtxt: callback(inputtxt))
inputBox = Entry(win, textvariable=inputtxt, width=25, font=('Arial', 40))
inputBox.pack()

printButton = Button(win, bg='pink', font=('Arial', 25), text="RUN", command=morseCode, height=2, width=15)
printButton.pack()

exitButton = Button(win, text="Exit", font=('Arial', 25), command=Exit, bg="grey", height=1, width=10)
exitButton.pack()

win.mainloop()
