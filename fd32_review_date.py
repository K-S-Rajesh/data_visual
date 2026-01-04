import os
import tkinter as tk
import time
import pyautogui as pag


cust=[
"217045",
"210399",
"207093",
"188271",
"187706",
"135576",
"124977",
"124952"
]
pag.hotkey('alt', 'tab')
time.sleep(3)

for i in range(8):
    time.sleep(5)
    pag.write(cust[i])
    time.sleep(1)

    # pag.write((pag.prompt(text='Enter RO code', title='MSG Box' , default='')),interval=0.3)
    time.sleep(2)
    pag.press('enter')
    time.sleep(1)
    pag.press('del', presses=10)
    time.sleep(1)
    pag.write('2000000')
    time.sleep(0.5)
    for i in range(7):
        pag.press('tab')
        time.sleep(0.3)
    pag.press('del', presses=10)
    time.sleep(1)

    pag.write('31.03.9999')
    time.sleep(1)

    pag.hotkey('ctrl', 's')
    time.sleep(1)
    # pag.press('enter')
    time.sleep(0.3)
    # pag.press('enter')
    # time.sleep(0.3)

    # pag.press('enter')
    # time.sleep(0.3)


