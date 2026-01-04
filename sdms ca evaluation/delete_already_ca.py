import pyautogui as pag
import time


pag.hotkey('alt','tab')
time.sleep(1)

for i in range(8):
    pag.click(x=952, y=691)
    time.sleep(3)
    pag.click(x=1446, y=540)
    time.sleep(3)
    pag.press('enter')
    time.sleep(5)

