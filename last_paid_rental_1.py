import os
import tkinter as tk
import time
import pyautogui as pag




pag.hotkey('alt','tab')
time.sleep(2)


for i in range(3):
    pag.hotkey('shift','tab')
    time.sleep(1)

pag.press('k',presses=2)
time.sleep(2)
# pag.hotkey('alt','down')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('r')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.hotkey('alt','down')
time.sleep(1)
pag.press('down',presses=4)
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('enter')


