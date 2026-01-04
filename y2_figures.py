import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(1)

for i in range(6):
    pag.hotkey('shift','right')
    time.sleep(1)
    pag.hotkey('ctrl','c')
    time.sleep(1)
    pag.press('left')
    time.sleep(1)
    pag.press('left')
    time.sleep(1)
    pag.hotkey('ctrl','v')
    time.sleep(1)
    pag.press('down')
    time.sleep(1)
    pag.press('right')
    time.sleep(1)
    pag.press('right')