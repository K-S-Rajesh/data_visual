import pyautogui as pag
import subprocess
import time
import os
import sys

pag.hotkey('alt', 'tab')
time.sleep(2)
cust=[
"208096",
"272261",
"125128",
"289385",
"180523",
"207065",
"188266",
"217028",
"188269",
"311234",
"124977",
"291447",
"197786",
"124956",
"124976",
"187721",
"208908",
"124966",
"208226",
"215272",
"124963",
"200435",
"133462",

]
x=len(cust)
for i in range(x):

    pag.press('tab')
    time.sleep(1)
    pag.write('23032025')
    time.sleep(1)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.write('23032025')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.press('space')
    time.sleep(2)
    pag.write('hoarding.png')
    time.sleep(2)
    pag.press('enter')
    time.sleep(5)
    pag.press('tab', presses=2)
    time.sleep(3)
    pag.write('complied')
    time.sleep(3)
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
    pag.click(x=1496,y=459)
    time.sleep(3)
    pag.scroll(-200)
    time.sleep(3)
    pag.scroll(-800)
    time.sleep(2)
    i=1
    while i<=1:
        #im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("hoarding_icon.png", confidence=0.7)
            pag.click(x,y)
        except TypeError:
            pag.click(x=1496, y=459)
            time.sleep(3)
            pag.scroll(-100)
            time.sleep(3)
            x, y = pag.locateCenterOnScreen("hoarding_icon.png", confidence=0.7)
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



