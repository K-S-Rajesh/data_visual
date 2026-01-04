import pyautogui as pag
import time

pag.hotkey('alt', 'tab')
time.sleep(2)
i=1
while i<= 1:
    # im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("hmsicon.png", confidence=0.7)
        pag.click(x, y)
    except TypeError:
        i = 1
    else:
        break
