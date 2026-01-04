import pyautogui as pag
import subprocess
import time
import os
import sys

pag.hotkey('alt', 'tab')
time.sleep(2)

i=1
while i<=1:
      #im = pag.screenshot("Full screen.png")
    try:
            x, y = pag.locateCenterOnScreen("activity_pend.png", confidence=0.7)
            pag.click(x,y)
    except TypeError:
            i = 1
    else:
            break


time.sleep(1)
pag.click(x=938, y=233)
time.sleep(0.5)

for i in range(5):
    pag.press('tab')
    time.sleep(0.3)

for i in range(18):
    pag.press('y')
    time.sleep(0.1)
    pag.press('tab')

time.sleep(2)
pag.press('space')
time.sleep(3)
pag.click(x=1227, y=241)
