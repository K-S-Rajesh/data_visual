import pyautogui as pag
import time

pag.hotkey('alt','tab')

# Section 1
for i in range(10):
    pag.press('tab',presses=5)
    time.sleep(.3)
    pag.press('up',presses=2)

# for i in range(19):
#     time.sleep(.5)
#     pag.press('n')
#     time.sleep(.5)
#     pag.press('tab', presses=2)