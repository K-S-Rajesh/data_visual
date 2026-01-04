
import webbrowser
import pyautogui as pag
import time
import os
import random




pag.hotkey('alt','tab')
#pag.press('tab')
# Section 1

for i in range(4):

    for i in range(7):
        for i in range(random.randint(3,4)):
            time.sleep(2)
            pag.press('down')
            time.sleep(2)

        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)

    time.sleep(1)

    pag.click(989, 962)
    time.sleep(1)

    pag.click(326, 840)
    time.sleep(1)

    for i in range(2):
        time.sleep(1)
        pag.press('down')
        time.sleep(1)
        pag.press('down')
        time.sleep(1)
        pag.press('down')


        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')
        time.sleep(2)
        pag.press('tab')

    time.sleep(5)

    pag.click(932, 369)
    time.sleep(5)

    pag.press('pagedown')

    time.sleep(2)

    pag.click(376, 615)
    time.sleep(5)






