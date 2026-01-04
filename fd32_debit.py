import os
import tkinter as tk
import time
import pyautogui as pag





pag.hotkey('alt','tab')
time.sleep(3)

pag.write((pag.prompt(text='Enter RO code', title='MSG Box' , default='')),interval=0.3)
time.sleep(2)
pag.press('enter')
time.sleep(1)
pag.press('del',presses=10)
time.sleep(1)


for i in range(7):
    pag.press('tab')
    time.sleep(0.3)
pag.press('del',presses=10)
time.sleep(1)

pag.write('31.12.2023')
time.sleep(1)

for i in range(5):
    pag.press('tab')
    time.sleep(0.3)
pag.press('del',presses=10)
time.sleep(1)

pag.write('31.03.2024')
time.sleep(1)

pag.hotkey('ctrl','s')
time.sleep(1)
pag.press('enter')
time.sleep(0.3)
pag.press('enter')
time.sleep(0.3)

pag.press('enter')
time.sleep(0.3)
