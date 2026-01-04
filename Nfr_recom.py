import os
import tkinter as tk
import time
import pyautogui as pag



pag.hotkey('alt','tab')
time.sleep(2)


n=int((pag.prompt(text='How many days you wish to recommend', title='MSG Box' , default='')))


for i in range(n):
    for i in range(9):
        pag.press('tab')
        time.sleep(0.2)

    pag.press('space')
    time.sleep(15)

    for i in range(9):
        pag.press('tab')
        time.sleep(0.2)
    time.sleep(1)
    pag.press('down',presses=3)
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.write('Recommended for Approval')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(30)

