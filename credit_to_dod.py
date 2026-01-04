import os
import tkinter as tk
import time
import pyautogui as pag




time.sleep(10)

for i in range(10):
    pag.hotkey('ctrl','c')
    time.sleep(2)
    pag.hotkey('alt','tab')
    time.sleep(2)
    pag.hotkey('ctrl', 'v')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('backspace')
    time.sleep(2)
    pag.press('down')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.hotkey('ctrl','s')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.hotkey('alt','tab')
    time.sleep(2)
    pag.press('down')
    time.sleep(2)




