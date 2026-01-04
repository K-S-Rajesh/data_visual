import pyautogui as pag
import time
import random as rd

pag.hotkey('alt','tab')
time.sleep(1)
# pag.press('space')
pag.press('down')
time.sleep(0.5)
for k in range(rd.randint(1,3)):
        pag.press('down')
        time.sleep(0.25)
pag.press('enter')
time.sleep(2)



for i in range(6):
    for j in range(5):
        pag.press('tab')
        time.sleep(1.5)
    pag.press('down')
    time.sleep(0.5)
    for k in range(rd.randint(1,3)):
        pag.press('down')
        time.sleep(0.25)
    pag.press('enter')
    time.sleep(2)

pag.hotkey('alt','.')
time.sleep(1)
pag.press('down')
time.sleep(0.5)
for k in range(rd.randint(1,3)):
        pag.press('down')
        time.sleep(0.25)
pag.press('enter')
time.sleep(2)
time.sleep(1)
pag.hotkey('alt','.')
pag.press('down')
time.sleep(0.5)
for k in range(rd.randint(1,3)):
        pag.press('down')
        time.sleep(0.25)
pag.press('enter')
time.sleep(2)
