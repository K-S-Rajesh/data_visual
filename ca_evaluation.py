import webbrowser
import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(1)
pag.press('space')
for i in range(7):
    pag.press('tab',presses=3)
    pag.press('space')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('space')



