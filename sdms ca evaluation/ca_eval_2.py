import pyautogui as pag
import time
import random as rd

pag.hotkey('alt','tab')
time.sleep(1)
# pag.press('space')
for j in range(8):
    pag.press('down')
    time.sleep(0.5)
    for k in range(rd.randint(1,3)):
            pag.press('down')
            time.sleep(0.25)
    pag.press('enter')
    time.sleep(2)

    for i in range(8):
        pag.hotkey('alt','.')
        time.sleep(3)
        pag.press('down')
        time.sleep(0.5)
        for k in range(rd.randint(1,3)):
            pag.press('down')
            time.sleep(0.25)
        pag.press('enter')
        time.sleep(2)
    time.sleep(2)
    pag.click(x=959, y=372)
    time.sleep(10)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.click(x=337, y=602)
    time.sleep(1)









