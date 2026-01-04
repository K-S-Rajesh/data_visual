import os
import tkinter as tk
import time
import sys
import pyautogui as pag
import pandas as pd
import numpy as np
import openpyxl



os.system('start sapshcut.exe -system=PRD -client=310 -user=00501203 -pw=Epicon@123')



i=1
while i<=1:
    #im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("saplogonentry.png", confidence=0.7)
    except TypeError:
        i = 1
    else:
        break


time.sleep(1)
pag.hotkey('alt','space')
time.sleep(0.3)
pag.press('x')
time.sleep(1)

pag.hotkey('ctrl', '/')
time.sleep(1)
pag.write('/nfd32')
time.sleep(1)
pag.press('enter')
time.sleep(2)



