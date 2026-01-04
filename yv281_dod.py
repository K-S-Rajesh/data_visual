import os
import tkinter as tk
import time
import pyautogui as pag

pag.hotkey('alt', 'tab')
time.sleep(3)

for i in range(5):

    pag.hotkey('ctrl','/')
    time.sleep(0.5)
    pag.write('/nyv281')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(5)
    pag.hotkey('ctrl','tab')
    time.sleep(0.5)
    pag.hotkey('ctrl','tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.5)
    pag.write((pag.prompt(text='Enter RO code', title='MSG Box' , default='')),interval=0.3)
    time.sleep(1)
    pag.press('tab',presses=2)
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.hotkey('ctrl','tab')
    time.sleep(1)
    pag.hotkey('ctrl','tab')
    time.sleep(0.5)
    pag.hotkey('ctrl','tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write((pag.prompt(text='Enter 1DD/2DD', title='MSG Box' , default='')),interval=0.3)
    time.sleep(0.5)
    for i in range(14):
        pag.hotkey('shift','tab')
        time.sleep(0.3)

    pag.press('space')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.5)
    pag.press('tab',presses=3)
    time.sleep(0.5)
    pag.press('space')
