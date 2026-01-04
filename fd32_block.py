import os
import tkinter as tk
import time
import sys
import pyautogui as pag
import pandas as pd
import numpy as np
import openpyxl
from pyautogui import ImageNotFoundException

#os.system('start sapshcut.exe -system=PRD -client=310 -user=00501203 -pw=Vomer@123')
#time.sleep(5)
#i=1
#while i<=1:
    #im = pag.screenshot("Full screen.png")
#    try:
 #       x, y = pag.locateCenterOnScreen("sap_logon.png", confidence=0.7)
  #  except TypeError:
   #     i = 1
   # else:
    #    break


# time.sleep(10)
# pag.hotkey('alt','space')
# time.sleep(0.3)
# pag.press('x')
# time.sleep(1)
pag.hotkey('alt', 'tab')
time.sleep(1)
pag.hotkey('ctrl', '/')
time.sleep(1)
pag.write('/nfd32')
time.sleep(1)
pag.press('enter')
time.sleep(2)



cust=[
"187713",
"187721",
"200435",
"273981",
"290025",
"124956",
"124958",
"197735",
"212532",
"221834",
"133458",
"291447"

]


x=len(cust)
#print(x)

# time.sleep(2)
pag.write(cust[0])
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write('c004')
time.sleep(1)
pag.press('tab',presses=4)
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.hotkey('ctrl','s')


#sys.exit()

for i in range(x):
    time.sleep(5)
    pag.write(cust[i+1])
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.hotkey('ctrl','tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.hotkey('ctrl','s')
    time.sleep(2)


    j = 1
    while j <= 1:
        try:
            x, y = pag.locateCenterOnScreen("customer_code.png", confidence=0.5)
            time.sleep(2)
            pag.moveTo(x,y)
            print('i found it')
            j=j+1
        except ImageNotFoundException:
            time.sleep(2)
            pag.press('enter')
            time.sleep(2)
            j = 1
        else:
            break
























