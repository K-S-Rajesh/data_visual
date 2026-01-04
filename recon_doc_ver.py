import pyautogui as pag
import subprocess
import time
import os
import sys



pag.hotkey('alt','tab')
# pag.press('tab')


for j in range(8):
    for i in range(4):
        pag.press('down')
        time.sleep(1)
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    for i in range(2):
        pag.press('down')
        time.sleep(1)
    pag.press('tab')
    time.sleep(8)

