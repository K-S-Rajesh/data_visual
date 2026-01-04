import os
import tkinter as tk
import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(2)
for i in range(10):
    pag.press('down')
    time.sleep(2)
    pag.press('space')
    time.sleep(2)
