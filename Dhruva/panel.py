import pyautogui as pag
import subprocess
import time
import os
import sys

pag.hotkey('alt', 'tab')
time.sleep(2)

cust=[
"187731"

]
x=len(cust)
for i in range(x):

    pag.press('tab')
    time.sleep(0.3)
    pag.write('22102024')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.write('22102024')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.press('space')
    time.sleep(4)
    pag.write('panel.png')
    time.sleep(3)
    pag.press('enter')
    time.sleep(5)
    pag.press('tab', presses=2)
    time.sleep(4)
    pag.write('complied')
    time.sleep(3)
    pag.press('tab')
    time.sleep(3)
    pag.press('space')
    time.sleep(3)
    pag.click(x=1412, y=237)
    time.sleep(1)
    pag.hotkey('fn', 'pageup')
    time.sleep(1)
    pag.click(x=483, y=511)
    pag.press('del', presses=10)
    time.sleep(2)
    pag.write(cust[i])
    time.sleep(3)
    pag.click(x=813, y=640)
    time.sleep(30)
    pag.click(x=1415, y=572)
    time.sleep(3)
    # pag.scroll(-90)
    time.sleep(3)
    # pag.scroll(-200)
    time.sleep(2)
    i=1
    while i<=1:
        #im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("panelicon.png", confidence=0.8)
            pag.click(x,y)
        except TypeError:
            i = 1
        else:
            break

    time.sleep(3)
    # pag.write(pag.prompt(text='Should i continue', title='' , default=''))
    # time.sleep(3)
    # pag.press('tab')
    # time.sleep(0.5)
    # pag.press('space')
    # pag.hotkey('alt','tab')
    # time.sleep(2)
    # pag.hotkey('shift','f10')
    # time.sleep(1)
    # pag.press('enter')



