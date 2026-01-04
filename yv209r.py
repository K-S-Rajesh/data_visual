import pyautogui as pag
from datetime import date, timedelta
import time
import subprocess
from pynput.mouse import Button, Controller
mouse = Controller()
from tkinter import messagebox as mb
import sys

i=1
while i<=1:
    im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("Refreshrefresh.png", confidence=0.7)
    except TypeError:
        i = 1
    else:
        mouse.position = (x, y)
        mouse.click(Button.left, 1)
        time.sleep(60)
sys.exit()
