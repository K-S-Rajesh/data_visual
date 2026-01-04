import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(3)
pag.press('tab')

# Section 1
for i in range(28):
    time.sleep(.5)
    pag.write('automation problem')
    time.sleep(.5)
    pag.press('tab')
time.sleep(.3)
