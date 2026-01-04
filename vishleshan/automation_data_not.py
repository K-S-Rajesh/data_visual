#before running this program ensure that vishleshan is open in chrome window and if u press alt+tab, the landing screen should be vishleshan

import pyautogui as pag
import time




pag.hotkey('alt','tab')
time.sleep(1)

for j in range(3):
    pag.click(x=870, y=580)
    time.sleep(10)
    pag.click(x=1721, y=443)
    time.sleep(7)
    pag.click(x=1474, y=262)
    time.sleep(3)

    for i in range(8):
            pag.press('tab')
            time.sleep(1)

    pag.press('n')
    time.sleep(1)
    pag.press('tab')
    time.sleep(10)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.write('recommended for closure in view of justification given by Automation Engineer')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    # pag.press('tab')
    # time.sleep(1)
    pag.press('space')
    time.sleep(3)
    pag.press('space')
    time.sleep(4)
    pag.click(x=740, y=25)
    time.sleep(4)
    pag.click(x=1379, y=411)
    time.sleep(3)
