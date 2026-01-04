import pyautogui as pag
import subprocess
import time
import os
import sys

from pyautogui import ImageNotFoundException

pag.hotkey('alt', 'tab')
time.sleep(2)

cust=[
"187720",
"198725",
"124994"

]
x=len(cust)
for i in range(x):

    pag.press('tab')
    time.sleep(0.3)
    pag.write('23032025')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.write('23032025')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.press('space')
    time.sleep(2)
    pag.write('signage.jpg')
    time.sleep(2)
    pag.press('enter')
    time.sleep(5)
    pag.press('tab', presses=2)
    time.sleep(1)
    pag.write('complied')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(3)
    pag.click(x=1511, y=266)
    time.sleep(1)
    pag.hotkey('fn', 'pageup')
    time.sleep(1)
    pag.click(x=735, y=610)
    pag.press('backspace',presses=10)
    time.sleep(2)
    pag.write(cust[i])
    time.sleep(3)
    pag.click(x=961, y=826)
    time.sleep(30)
    pag.click(x=1505,y=593)
    time.sleep(3)
    pag.scroll(-200)
    time.sleep(3)
    pag.scroll(-200)
    time.sleep(2)
    i=1
    while i<=1:
        #im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("signage_icon.png", confidence=0.7)
            pag.click(x,y)
        except ImageNotFoundException:
            time.sleep(3)
            pag.scroll(-800)
            time.sleep(3)
            x, y = pag.locateCenterOnScreen("signage_icon.png", confidence=0.7)
            pag.click(x, y)
            i = 1
        else:
            break

    time.sleep(1)
    # pag.write(pag.prompt(text='Should i continue', title='' , default=''))
    # time.sleep(3)
    # pag.press('tab')
    # time.sleep(0.5)
    # pag.press('space')
    # pag.hotkey('alt','tab')
    # time.sleep(2)
    # pag.hotkey('shift','f10')
    # time.sleep(1)
    # press('enter')

