import os
import tkinter as tk
import time
import pyautogui as pag



pag.hotkey('alt', 'tab')
time.sleep(2)

pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nyfio')
time.sleep(1)
pag.press('enter')
time.sleep(1)


for i in range(2):
    pag.hotkey('ctrl','tab')
    time.sleep(2)

time.sleep(1)
pag.press('enter')
time.sleep(0.3)
pag.write('4200')
time.sleep(0.3)
pag.press('f8')
time.sleep(5)
for j in range(1):
    x, y = pag.locateCenterOnScreen("add_io.png", confidence=0.6)
    pag.click(x, y)
    time.sleep(0.5)
    pag.write('12')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('space')
    time.sleep(0.5)
    # pag.hotkey('ctrl','/')
    # time.sleep(0.5)
