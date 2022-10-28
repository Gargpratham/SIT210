from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

redLed = LED(5)
blueLed = LED(6)      
greenLed = LED(13)

win = Tk()
win.geometry('350x200')
win.title("Radio Buttons LED toggler")
myFont = tkinter.font.Font(family = 'Arial', size = 20, weight = "bold")
var = IntVar()

def LEDtoggles():
    v = var.get()
    if v == 1:
        redLed.on()
        blueLed.off()
        greenLed.off()
    elif v == 2:
        blueLed.on()
        greenLed.off()
        redLed.off()
    elif v == 3:
        greenLed.on()
        redLed.off()
        blueLed.off()
    elif v == 4:
        redLed.on()
        blueLed.on()
        greenLed.on()
    else:
        redLed.off()
        blueLed.off()
        greenLed.off()
        
def LEDexit():
    GPIO.cleanup()
    win.destroy()

red = Radiobutton(win, text = "Red", font = myFont, variable = var, value = 1, command = LEDtoggles, bg = "red", height = 1, width = 20)
red.grid(row = 1, column = 0)

blue = Radiobutton(win, text = "Blue", font = myFont, variable = var, value = 2, command = LEDtoggles, bg = "RoyalBlue1", height = 1, width = 20)
blue.grid(row = 2, column = 0)

green = Radiobutton(win, text = "Green", font = myFont, variable = var, value = 3, command = LEDtoggles, bg = "green", height = 1, width = 20)
green.grid(row = 3, column = 0)

All = Radiobutton(win, text = "All", font = myFont, variable = var, value = 4, command = LEDtoggles, bg = "violet", height = 1, width = 20)
All.grid(row = 4, column = 0)

Exit = Button(win, text = "Exit", font = myFont, command = LEDexit, bg = "grey", height = 1, width = 5)
Exit.grid(row = 5, column = 0)

win.protocol("WM_DELETE_WINDOW")
win.mainloop()
