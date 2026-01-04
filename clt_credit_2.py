import os
import tkinter as tk
import time
import pyautogui as pag


pag.hotkey('alt','tab')
time.sleep(2)
pag.hotkey('ctrl','/')
time.sleep(2)
pag.write('/nyv281')
time.sleep(1)
pag.press('enter')
time.sleep(5)

for i in range(3):
    pag.hotkey('ctrl','tab')
    time.sleep(1)

pag.press('enter')
time.sleep(1)
pag.write((pag.prompt(text='Enter RO code', title='MSG Box' , default='')),interval=0.3)
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(3)
for i in range(11):
    pag.press('tab')
    time.sleep(0.3)





#for i in range(2):
#    pag.hotkey('ctrl','tab')
#    time.sleep(1)

#pag.press('tab')
#time.sleep(1)
#pag.press('tab')
#time.sleep(1)
pag.write('900')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
for i in range(2):
    pag.hotkey('ctrl','tab')
    time.sleep(1)
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.press('tab',presses=3)
time.sleep(1)
pag.press('space')

