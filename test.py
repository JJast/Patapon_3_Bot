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
pyautogui.moveTo(650, 1400)
pyautogui.click()

# Main loop
try:
    while True:
        # Initiate rythm
        while pyautogui.pixel(1721,1378) [0] == 127:
            if pyautogui.pixel(377, 1411) [0] == 166:
                time.sleep(0.29)
                for i in range (7):
                    pyautogui.keyDown('x')
                    time.sleep(0.12)
                    pyautogui.keyUp('x')
                    time.sleep(0.351)
                    pyautogui.keyDown('x')
                    time.sleep(0.12)
                    pyautogui.keyUp('x')
                    time.sleep(0.351)
                    pyautogui.keyDown('a')
                    time.sleep(0.12)
                    pyautogui.keyUp('a')
                    time.sleep(0.351)
                    pyautogui.keyDown('x')
                    time.sleep(0.12)
                    pyautogui.keyUp('x')
                    time.sleep(2.352)

                    pyautogui.keyDown('a')
                    time.sleep(0.12)
                    pyautogui.keyUp('a')
                    time.sleep(0.351)
                    pyautogui.keyDown('a')
                    time.sleep(0.12)
                    pyautogui.keyUp('a')
                    time.sleep(0.351)
                    pyautogui.keyDown('a')
                    time.sleep(0.12)
                    pyautogui.keyUp('a')
                    time.sleep(0.351)
                    pyautogui.keyDown('x')
                    time.sleep(0.12)
                    pyautogui.keyUp('x')
                    time.sleep(2.352)
        
        # Chest opening
        while pyautogui.pixel(377,1411) [0] == 159:
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.3)
            pyautogui.keyDown('q')
            time.sleep(0.01)
            pyautogui.keyUp('q')
            time.sleep(0.5)
        
        # Skip lvl
        while pyautogui.pixel(58, 1323) [0] == 239:
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.3)
        
        # Loading screen
        if pyautogui.pixel(1803,1390) [0] == 196:
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.2)

        # Go to next mission
        if pyautogui.pixel(1276,1161) [0] == 206:
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
            
except KeyboardInterrupt:
    print('\n')


