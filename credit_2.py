import os
import tkinter as tk
import time
import sys
import pyautogui as pag
#WIDTH = 200

#HEIGHT = 300

#root = tk.Tk()

#canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

#canvas.pack()x

#def myClick1():

os.system('start sapshcut.exe -system=PRD -client=310 -user=00036422 -pw=Positive@2')

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
#sys.exit()
pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nyvrce')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.write('4103')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(1)
sys.exit()
pag.hotkey('ctrl','v')





