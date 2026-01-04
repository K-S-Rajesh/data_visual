import webbrowser
import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(3)
pag.press('tab',presses=2)
for i in range(24):
    pag.press('down')
    time.sleep(0.3)
    pag.press('tab')
time.sleep(2)
pag.press('tab',presses=2)
time.sleep(1)
pag.press('space')
