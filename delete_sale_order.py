import os
import tkinter as tk
import time
import sys
import pyautogui as pag
import pandas as pd
import numpy as np
import openpyxl






sale_order=[
"373584400",
"373612167",
"373616402",
"373548035"
]



pag.hotkey('alt','tab')
time.sleep(3)


pag.hotkey('ctrl', '/')
time.sleep(1)
pag.write('/nva02')
time.sleep(1)
pag.press('enter')
time.sleep(2)


for i in range(4):
    time.sleep(5)
    pag.write(sale_order[i])
    time.sleep(3)
    pag.press('enter')
    time.sleep(2)
    pag.press('alt')
    time.sleep(2)
    pag.press('e')
    time.sleep(1)
    pag.press('tab',presses=2)
    time.sleep(1)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)





