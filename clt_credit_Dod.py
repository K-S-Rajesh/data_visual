import os
import tkinter as tk
import time
import pyautogui as pag
from pyautogui import ImageNotFoundException

pag.hotkey('alt','tab')



cust=[
#"277552",
#"187726",
#"188269",
"328648",
"352928",
"353705",
"352137",
"337727",
"217849",
"374566"


]
x=len(cust)
for i in range(x):
    pag.write(cust[i])
    time.sleep(2)
    pag.press('enter')
    time.sleep(4)
    pag.write('3000000')
    time.sleep(1)
    pag.press('tab', presses=7)
    time.sleep(0.3)
    pag.write('31032026')
    time.sleep(0.3)
    pag.hotkey('ctrl','s')
    time.sleep(3)

    i=1
    while i<=1:
        #im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("fd32.png", confidence=0.7)
            #pag.click(x,y)
        except ImageNotFoundException:
            pag.press('enter')
            time.sleep(3)
            i = 1
        else:
            break

    time.sleep(3)
    # pag.scroll(-30)
    # time.sleep(3)
    # i = 1
    # while i <= 1:
    #     # im = pag.screenshot("Full screen.png")
    #     try:
    #         x, y = pag.locateCenterOnScreen("canopy.png", confidence=0.7)
    #         pag.click(x, y)
    #     except TypeError:
    #         i = 1
    #     else:
    #         break

    time.sleep(1)
    # pag.write(pag.prompt(text='Should i continue', title='' , default=''))
    time.sleep(1)
    # pag.hotkey('alt','tab')
    # time.sleep(2)
    # pag.hotkey('shift','f10')
    # time.sleep(1)
    # pag.press('enter')

