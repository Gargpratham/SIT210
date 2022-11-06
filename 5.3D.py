from tkinter import *
from time import sleep
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

LED = LED(5)

win = Tk()
win.title("Morse code")


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

inputtxt = StringVar()

def callback(inputtxt):
    value = inputtxt.get()
    if len(value) > 12: inputtxt.set(value[:12])


def morseCode():
    value = inputBox.get()
    value = value.upper()
    for letter in value:
        if (letter == ' '):
            sleep(4)

        elif (letter == 'A'):
            print(".-", end=" ")
            dot()
            dash()

        elif (letter == 'B'):
            print("-...", end=" ")
            dash()
            dot()
            dot()
            dot()

        elif (letter == 'C'):
            print("-.-.", end=" ")
            dash()
            dot()
            dash()
            dot()

        elif (letter == 'D'):
            print("-..", end=" ")
            dash()
            dot()
            dot()

        elif (letter == 'E'):
            print(".", end=" ")
            dot()

        elif (letter == 'F'):
            print("..-.", end=" ")
            dot()
            dot()
            dash()
            dot()

        elif (letter == 'G'):
            print("--.", end=" ")
            dash()
            dash()
            dot()

        elif (letter == 'H'):
            print("....", end=" ")
            dot()
            dot()
            dot()
            dot()

        elif (letter == 'I'):
            print("..", end=" ")
            dot()
            dot()

        elif (letter == 'J'):
            print(".---", end=" ")
            dot()
            dash()
            dash()
            dash()

        elif (letter == 'K'):
            print("-.-", end=" ")
            dash()
            dot()
            dash()

        elif (letter == 'L'):
            print(".-..", end=" ")
            dot()
            dash()
            dot()
            dot()

        elif (letter == 'M'):
            print("--", end=" ")
            dash()
            dash()

        elif (letter == 'N'):
            print("-.", end=" ")
            dash()
            dot()

        elif (letter == 'O'):
            print("---", end=" ")
            dash()
            dash()
            dash()

        elif (letter == 'P'):
            print(".--.", end=" ")
            dot()
            dash()
            dash()
            dot()

        elif (letter == 'Q'):
            print("--.-", end=" ")
            dash()
            dash()
            dot()
            dash()

        elif (letter == 'R'):
            print(".-.", end=" ")
            dot()
            dash()
            dot()

        elif (letter == 'S'):
            print("...", end=" ")
            dot()
            dot()
            dot()

        elif (letter == 'T'):
            print("-", end=" ")
            dash()

        elif (letter == 'U'):
            print("..-", end=" ")
            dot()
            dot()
            dash()

        elif (letter == 'V'):
            print("...-", end=" ")
            dot()
            dot()
            dot()
            dash()

        elif (letter == 'W'):
            print(".--", end=" ")
            dot()
            dash()
            dash()

        elif (letter == 'X'):
            print("-..-", end=" ")
            dash()
            dot()
            dot()
            dash()

        elif (letter == 'Y'):
            print("-.--", end=" ")
            dash()
            dot()
            dash()
            dash()

        elif (letter == 'Z'):
            print("--..", end=" ")
            dash()
            dash()
            dot()
            dot()

        elif (letter == '1'):
            print(".----", end=" ")
            dot()
            dash()
            dash()
            dash()
            dash()

        elif (letter == '2'):
            print("..---", end=" ")
            dot()
            dot()
            dash()
            dash()
            dash()

        elif (letter == '3'):
            print("...--", end=" ")
            dot()
            dot()
            dot()
            dash()
            dash()

        elif (letter == '4'):
            print("....-", end=" ")
            dot()
            dot()
            dot()
            dot()
            dash()

        elif (letter == '5'):
            print(".....", end=" ")
            dot()
            dot()
            dot()
            dot()
            dot()

        elif (letter == '6'):
            print("-....", end=" ")
            dash()
            dot()
            dot()
            dot()
            dot()

        elif (letter == '7'):
            print("--...", end=" ")
            dash()
            dash()
            dot()
            dot()
            dot()

        elif (letter == '8'):
            print("---..", end=" ")
            dash()
            dash()
            dash()
            dot()
            dot()

        elif (letter == '9'):
            print("----.", end=" ")
            dash()
            dash()
            dash()
            dash()
            dot()

        elif (letter == '0'):
            print("-----", end=" ")
            dash()
            dash()
            dash()
            dash()
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