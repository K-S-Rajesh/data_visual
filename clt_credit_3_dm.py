import os
import tkinter as tk
import time
import pyautogui as pag

os.system('start sapshcut.exe -system=PRD -client=310 -user=00081845 -pw=Password@1')


time.sleep(10)
pag.hotkey('alt','space')
time.sleep(0.3)
pag.press('x')
time.sleep(3)
pag.hotkey('ctrl','/')
time.sleep(3)
pag.write('/nyv281')
time.sleep(1)
pag.press('enter')
time.sleep(4)

for i in range(5):
    pag.hotkey('ctrl','tab')
    time.sleep(1)
pag.press('enter')
time.sleep(1)
