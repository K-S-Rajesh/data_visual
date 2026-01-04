import pyautogui as pag
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import sys


pag.hotkey('alt','tab')
time.sleep(3)

#for i in range(20):
#    pag.press('enter')
#    time.sleep(8)


i=1
while i<=1:
    im = pag.screenshot("Full_screen.png")
    try:
        x, y = pag.locateCenterOnScreen("return_1.png", confidence=0.7)
    except TypeError:
        i = 1
        pag.press('enter')
        time.sleep(8)
    else:
        mouse.position = (x, y)
        mouse.click(Button.left, 1)
        time.sleep(4)
        sys.exit()


















































































