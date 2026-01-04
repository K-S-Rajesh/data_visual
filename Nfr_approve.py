import os
import tkinter as tk
import time
import pyautogui as pag



pag.hotkey('alt','tab')
time.sleep(2)


n=int((pag.prompt(text='How many days you wish to Approve', title='MSG Box' , default='')))


for i in range(n):
    for i in range(10):
        pag.press('tab')
        time.sleep(0.2)

    pag.press('space')
    time.sleep(30)

    for i in range(10):
        pag.press('tab')
        time.sleep(0.2)
    time.sleep(1)
    pag.press('down',presses=3)
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.write('Approved')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)

