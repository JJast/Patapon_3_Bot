import time, pyautogui

try:
    while True:
        px = pyautogui.pixel(977, 1036)
        print(px)
        time.sleep(0.05)        
except KeyboardInterrupt:
    print('\n')