from sys import float_repr_style
import time, pyautogui, random
from pywinauto.keyboard import send_keys
import keyboard

# pyautogui.displayMousePosition()

# try:
#     while True:
#         px = pyautogui.pixel(127, 1352)
#         print(px)
#         time.sleep(0.05)        
# except KeyboardInterrupt:
#     print('\n')


# Open PPSSPP
pyautogui.moveTo(940, 1050)
pyautogui.click()

# PIXEL LIST (Position X, Position Y, Value of color red of Pixel)
levelPixel = (228, 1022, 128) # Pixel to determine if level is loaded
rythmPixel = (23, 1061, 142) # Pixel to determine rythm, red color value should be adjusted to the beat frame around the screen
chestPixel = (200, 900, 110) # Pixel to determine if chest opening is active
loadingPixel = (60, 90, 255) # Pixel to determine if loading screen is active
hubPixel = (956, 895, 191) # Pixel to determine if Patapon Hub is active (Patapon Base)
summaryPixel = (37, 998, 224) # Pixel to determine if level summary is active

# Timings - timings to adjust, probably best to leave it unchanged
pressdown = 0.01
buttonwait = 0.29
commandwait = 2.1
lastwait = 0.19
command_epoch = 20

STATE='' # State variable, used in debugging

def makecommand(button1, button2, button3, button4):
    pyautogui.keyDown(button1)
    time.sleep(pressdown)
    pyautogui.keyUp(button1)
    time.sleep(buttonwait)
    pyautogui.keyDown(button2)
    time.sleep(pressdown)
    pyautogui.keyUp(button2)
    time.sleep(buttonwait)
    pyautogui.keyDown(button3)
    time.sleep(pressdown)
    pyautogui.keyUp(button3)
    time.sleep(buttonwait)
    pyautogui.keyDown(button4)
    time.sleep(pressdown)
    pyautogui.keyUp(button4)
    time.sleep(lastwait)

def command(action):
    print('COMMAND TIME: ',time.time(), 'seconds')
    if action == 'attack':
        makecommand('x','x','a','x')
    if action == 'walk':
        makecommand('a','a','a','x')
    if action == 'defend':
        makecommand('s','s','a','x')

# Main loop
try:
    while True:
        if STATE != 'STATE: LOOKING FOR PIXELS':
            STATE='STATE: LOOKING FOR PIXELS'
            print(STATE)

       # Go to next mission
        if pyautogui.pixel(hubPixel[0],hubPixel[1]) [0] == hubPixel[2]:
            STATE='STATE: RUNNING NEXT MISSION'
            print(STATE)
            pyautogui.keyDown('w')
            time.sleep(0.01)
            pyautogui.keyUp('w')
            time.sleep(0.2)

            pyautogui.keyDown('w')
            time.sleep(0.01)
            pyautogui.keyUp('w')
            time.sleep(0.2)

            pyautogui.keyDown('z')
            time.sleep(0.05)
            pyautogui.keyUp('z')
            time.sleep(0.5)

            pyautogui.keyDown('z')
            time.sleep(0.05)
            pyautogui.keyUp('z')
            time.sleep(0.3)

            pyautogui.keyDown('up')
            time.sleep(0.02)
            pyautogui.keyUp('up')
            time.sleep(0.2)
            
            pyautogui.keyDown('z')
            time.sleep(0.05)
            pyautogui.keyUp('z')
            time.sleep(0.5)

            pyautogui.keyDown('space')
            time.sleep(0.05)
            pyautogui.keyUp('space')
            time.sleep(0.5)
            
            pyautogui.keyDown('up')
            time.sleep(0.05)
            pyautogui.keyUp('up')
            time.sleep(0.2)

            pyautogui.keyDown('z')
            time.sleep(0.05)
            pyautogui.keyUp('z')
            time.sleep(4)

            pyautogui.keyDown('z')
            time.sleep(0.05)
            pyautogui.keyUp('z')
            time.sleep(0.2)

        # Initiate rythm
        while pyautogui.pixel(levelPixel[0],levelPixel[1]) [0] == levelPixel[2]:
            STATE='STATE: INSIDE MISSION'
            print(STATE)
            if pyautogui.pixel(rythmPixel[0],rythmPixel[1]) [0] == rythmPixel[2]:
                STATE='STATE: FOUND RYTHM'
                print(STATE)
                time.sleep(0.29)
                for i in range (command_epoch):
                    command('attack')
                    time.sleep(commandwait)
                    command('walk')
                    time.sleep(commandwait)
        
        # Chest opening
        while pyautogui.pixel(chestPixel[0],chestPixel[1]) [0] == chestPixel[2]:
            STATE='STATE: CHEST OPENING'
            print(STATE)
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.3)
            pyautogui.keyDown('q')
            time.sleep(0.01)
            pyautogui.keyUp('q')
            time.sleep(0.5)
        
        # Skip lvl
        while pyautogui.pixel(summaryPixel[0],summaryPixel[1]) [0] == summaryPixel[2]:
            STATE='STATE: MISSION SUMMARY'
            print(STATE)
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.3)
        
        # Loading screen
        if pyautogui.pixel(loadingPixel[0],loadingPixel[1]) [0] == loadingPixel[2]:
            STATE='STATE: SKIPPING LOADING SCREEN'
            print(STATE)
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.2)

 
            
except KeyboardInterrupt:
    print('\n')


