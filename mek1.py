import os
import tkinter as tk
import time
import pyautogui as pag




pag.hotkey('alt','tab')
time.sleep(2)


cust=[
"352531",
"188259",
"124960",
"241821",
"133462",
"281505",
"376239",
"353549"

]



x=len(cust)
for i in range(x):
    time.sleep(2)
    pag.write(cust[i])
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('18000')
    time.sleep(2)
    pag.press('tab',presses=2)
    time.sleep(2)
    pag.write('4203')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('82.47')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('INR')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('1')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('kg')
    time.sleep(2)
    pag.press('tab',presses=2)
    time.sleep(2)
    pag.write('01.04.2025')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('31.12.9999')
    time.sleep(2)
    pag.hotkey('ctrl', 's')
    time.sleep(3)
    pag.press('tab')
    time.sleep(2)
    pag.press('enter')
    time.sleep(5)
    pag.hotkey('ctrl', '/')
    for i in range(1):
        pag.hotkey('ctrl','tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)



