import webbrowser
import pyautogui as pag
import time
import os


time.sleep(0.3)
pag.hotkey('alt','tab')



for i in range(7):
    time.sleep(2)
    pag.press('tab')
    time.sleep(.3)
    pag.press('space',presses=1)
    time.sleep(.3)
    pag.press('tab',presses=1)
    time.sleep(.3)
    pag.press('space')
    time.sleep(.3)
    pag.press('space')
    time.sleep(.3)
    pag.press('tab', presses=4)
    time.sleep(.3)
    pag.press('space')
    time.sleep(.3)
    pag.press('space')
    time.sleep(.3)
    pag.press('tab', presses=4)
    time.sleep(.3)
    pag.press('space',presses=1)
    time.sleep(15)
    pag.press('tab', presses=2)
    time.sleep(.3)
    pag.write('complied')
    time.sleep(.3)
    pag.press('tab', presses=1)
    time.sleep(.3)
    pag.press('space',presses=2)
    time.sleep(3)

time.sleep(.3)

