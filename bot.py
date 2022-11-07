import time, pyautogui, random

# pyautogui.displayMousePosition()

# try:
#     while True:
#         px = pyautogui.pixel(127, 1352)
#         print(px)
#         time.sleep(0.05)        
# except KeyboardInterrupt:
#     print('\n')


# Open PPSSPP
pyautogui.moveTo(650, 1760)
pyautogui.click()

# Main loop
try:
    while True:
        # Initiate rythm
        while pyautogui.pixel(1843,1621) [0] == 125:
            if pyautogui.pixel(2703,1508) [0] == 142:
                time.sleep(0.29)
                for i in range (5):

                    # pyautogui.keyDown('x')
                    # time.sleep(0.05)
                    # pyautogui.keyUp('x')
                    # time.sleep(0.23-(random.randint(-1,1))/100)
                    # pyautogui.keyDown('x')
                    # time.sleep(0.05)
                    # pyautogui.keyUp('x')
                    # time.sleep(0.23-(random.randint(-1,1))/100)
                    # pyautogui.keyDown('s')
                    # time.sleep(0.05-(random.randint(-1,1))/100)
                    # pyautogui.keyUp('s')
                    # time.sleep(0.23)
                    # pyautogui.keyDown('s')
                    # time.sleep(0.05-(random.randint(-1,1))/100)
                    # pyautogui.keyUp('s')
                    # time.sleep(2.14)

                    pyautogui.keyDown('x')
                    time.sleep(0.05)
                    pyautogui.keyUp('x')
                    time.sleep(0.23-(random.randint(-1,1))/100)
                    pyautogui.keyDown('x')
                    time.sleep(0.05)
                    pyautogui.keyUp('x')
                    time.sleep(0.23-(random.randint(-1,1))/100)
                    pyautogui.keyDown('a')
                    time.sleep(0.05-(random.randint(-1,1))/100)
                    pyautogui.keyUp('a')
                    time.sleep(0.23)
                    pyautogui.keyDown('x')
                    time.sleep(0.05-(random.randint(-1,1))/100)
                    pyautogui.keyUp('x')
                    time.sleep(2.14)

                    pyautogui.keyDown('a')
                    time.sleep(0.05)
                    pyautogui.keyUp('a')
                    time.sleep(0.23-(random.randint(-1,1))/100)
                    pyautogui.keyDown('a')
                    time.sleep(0.05)
                    pyautogui.keyUp('a')
                    time.sleep(0.23-(random.randint(-1,1))/100)
                    pyautogui.keyDown('a')
                    time.sleep(0.05-(random.randint(-1,1))/100)
                    pyautogui.keyUp('a')
                    time.sleep(0.23)
                    pyautogui.keyDown('x')
                    time.sleep(0.05-(random.randint(-1,1))/100)
                    pyautogui.keyUp('x')
                    time.sleep(2.14)

                    # pyautogui.keyDown('s')
                    # time.sleep(0.05)
                    # pyautogui.keyUp('s')
                    # time.sleep(0.23-(random.randint(-1,1))/100)
                    # pyautogui.keyDown('s')
                    # time.sleep(0.05)
                    # pyautogui.keyUp('s')
                    # time.sleep(0.23-(random.randint(-1,1))/100)
                    # pyautogui.keyDown('a')
                    # time.sleep(0.05-(random.randint(-1,1))/100)
                    # pyautogui.keyUp('a')
                    # time.sleep(0.23)
                    # pyautogui.keyDown('x')
                    # time.sleep(0.05-(random.randint(-1,1))/100)
                    # pyautogui.keyUp('x')
                    # time.sleep(2.14)
        

        # Chest opening
        while pyautogui.pixel(372,1654) [0] == 165:
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.3)
            pyautogui.keyDown('q')
            time.sleep(0.01)
            pyautogui.keyUp('q')
            time.sleep(0.5)
        
        # Skip lvl
        while pyautogui.pixel(52,1563) [0] == 227:
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.3)
        
        # Loading screen
        if pyautogui.pixel(2182,1610) [0] == 255 or pyautogui.pixel(2182,1610) [0] == 195 or pyautogui.pixel(2182,1610) [0] == 231:
            pyautogui.keyDown('z')
            time.sleep(0.01)
            pyautogui.keyUp('z')
            time.sleep(0.2)

        # Go to next mission
        if pyautogui.pixel(1362,1377) [0] == 211:
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

            
except KeyboardInterrupt:
    print('\n')


