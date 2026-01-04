import os
import tkinter as tk
import time
import pyautogui as pag




pag.hotkey('alt','tab')
time.sleep(3)
#a, b = pag.locateCenterOnScreen("deassign.png", confidence=0.7)

for i in range(40):

    pag.press('f9')
    time.sleep(2)
    pag.press('tab')
    time.sleep(1)
    pag.press('enter')
    time.sleep(3)





