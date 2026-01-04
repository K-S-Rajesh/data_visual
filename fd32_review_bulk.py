import os
import tkinter as tk
import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(3)

for i in range(140):

    for i in range(10):
        pag.press('down')
        time.sleep(0.3)

    time.sleep(3)
    pag.press('f2')
    time.sleep(3)
    pag.press('tab')
    time.sleep(3)
    pag.press('tab')
    time.sleep(2)
    pag.write('31.12.2025')
    time.sleep(2)
    pag.press('enter')
    time.sleep(7)



