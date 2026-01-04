import os
import tkinter as tk
import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(2)
for i in range(12):
    pag.press('down')
    time.sleep(3)
    pag.press('space')
    time.sleep(3)
    pag.write('Approval IInd 59 Outlets.pdf')
    time.sleep(3)
    pag.press('enter')
    time.sleep(10)



