import os
import tkinter as tk
import time
import sys
import pyautogui as pag
import pandas as pd
import numpy as np
import openpyxl



cust=[
"191286",
"133915",
"133885",
"133914",
"174936",
"133899",
"133758",
"262196",
"133902",
"269112",
"234306",
"183217",
"271965",
"189813",
"239910",
"336995",
"188171",
"269115",
"223657",
"188184",
"133908",
"180986",
"333660",
"133824",
"240263",
"340329",
"204360",
"315479",
"341435",
"133868",
"335725",
"216227",
"230822",
"342751",
"345455",
"271119",
"152624",
"133864",
"222098",
"310732"

]

x=len(cust)
print(x)

pag.hotkey('alt','tab')
for i in range(x):
    time.sleep(5)
    pag.write(cust[i])
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)

    j = 1
    while j <= 1:
        # im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("customercode.png", confidence=0.7)
        except TypeError:
            pag.hotkey('ctrl','s')
            time.sleep(1)
            pag.press('enter')
            time.sleep(1)
            j = 1
        else:
            break



    time.sleep(5)

