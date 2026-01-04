import subprocess
import pyautogui as pag
import time
import os
from datetime import date
from datetime import date,datetime,timedelta




pag.hotkey('alt', 'tab')
time.sleep(1)

for i in range(100):
    # pag.doubleClick(x=144, y=484) # first line item
    pag.doubleClick(x=157, y=522) #second line item
    time.sleep(0.75)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('30.04.2026')
    time.sleep(0.5)
    pag.hotkey('ctrl', 's')
    time.sleep(1)
