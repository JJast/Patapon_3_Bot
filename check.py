import time, pyautogui

try:
    while True:
        px = pyautogui.pixel(2703,1508)
        print(px)
        time.sleep(0.05)        
except KeyboardInterrupt:
    print('\n')