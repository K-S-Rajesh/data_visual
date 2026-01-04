import pyautogui as pag
import time
from pynput.mouse import Button, Controller
mouse = Controller()
import sys

i=1
while i<=1:
    im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("next.png", confidence=0.7)
    except TypeError:
        i = 1
    else:
        mouse.position = (x, y)
        mouse.click(Button.left, 1)
        time.sleep(2)

