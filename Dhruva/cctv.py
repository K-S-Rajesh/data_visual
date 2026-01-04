import pyautogui as pag
import subprocess
import time
import os
import sys

from pyautogui import ImageNotFoundException

pag.hotkey('alt', 'tab')
time.sleep(2)

cust=[
#"135376",
#"216240",
#"208907",
"135576",
"281505",
"282556",
"135023",
"124955",
"265744",
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
    time.sleep(3)
    pag.typewrite('cctv.png')
    time.sleep(5)
    pag.press('enter')
    time.sleep(10)
    pag.press('tab', presses=2)
    time.sleep(1)
    pag.typewrite('complied')
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
    pag.press('backspace', presses=10)
    time.sleep(2)
    pag.write(cust[i])
    time.sleep(3)
    pag.click(x=961, y=826)
    time.sleep(30)
    pag.click(x=1505, y=593)
    time.sleep(3)
    #pag.scroll(-200)

    #pag.press('tab', presses=2)
    # pag.click(x = 1332, y = 289)
    # time.sleep(1)
    #pag.scroll(-100)
    #time.sleep(1)
    i = 1
    while i <= 1:
        # im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("cctv_icon.png", confidence=0.7)
            pag.click(x, y)
        except ImageNotFoundException:
            pag.click(x=1505, y=593)
            time.sleep(3)
            pag.scroll(-100)
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

