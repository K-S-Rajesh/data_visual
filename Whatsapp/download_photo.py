import pyautogui as pag
import time


pag.hotkey('alt','tab')
time.sleep(2)

for i in range(50):
    pag.click(x=79, y=584)
    time.sleep(2)
    pag.click(x=1711, y=167)
    time.sleep(2)
