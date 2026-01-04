import pyautogui as pag
import time

#pag.hotkey('alt','tab')
time.sleep(1)

i=1
while i<=1:
    try:
        x, y = pag.locateCenterOnScreen("select_icon.png", confidence=0.7)
    except TypeError:
        i = 1
    else:
        pag.press('tab')
        time.sleep(1)
        pag.press('y')
        time.sleep(0.5)
        pag.press('tab')
        time.sleep(0.5)
        pag.press('y')
        time.sleep(0.5)
        pag.press('tab')
        time.sleep(0.5)
        pag.press('n')
        time.sleep(0.5)
        pag.press('tab')
        pag.press('space')
        time.sleep(1)
        pag.press('space')
        time.sleep(3)

sys.exit()
