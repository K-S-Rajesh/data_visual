import os
import tkinter as tk
import time
import pyautogui as pag


os.system('start sapshcut.exe -system=PRD -client=310 -user=00081845 -pw=Password@1')


time.sleep(10)
pag.hotkey('alt','space')
time.sleep(0.3)
pag.press('x')

pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nyvrce')
time.sleep(1)
pag.press('enter')
time.sleep(2)
pag.write('4203')
time.sleep(0.3)
pag.press('tab')
time.sleep(0.3)
pag.press('enter')
