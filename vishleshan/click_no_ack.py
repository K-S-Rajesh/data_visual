
import pyautogui as pag
import time
import sys

pag.hotkey('alt','tab')
time.sleep(1)
i=1
while i<=1:
    try:
        x,y = pag.locateCenterOnScreen("not_ack.png", confidence=0.8)
        #x,y=pag.center(location)
        pag.click(x,y+50)
    except TypeError:
        i = 1
    else:
        sys.exit()

# pag.moveRel(0, 1000, duration=0.5)
