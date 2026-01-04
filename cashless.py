import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(3)
pag.press('tab')

# Section 1
for i in range(2):
    time.sleep(.2)
    pag.press('n')
    time.sleep(.2)
    pag.press('tab')
    time.sleep(.2)
    pag.write('not available')
    time.sleep(.2)
    pag.press('tab')

time.sleep(.3)



