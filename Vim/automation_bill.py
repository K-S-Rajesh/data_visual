import time
import pyautogui as pag


pag.hotkey('alt','tab')
time.sleep(2)
for i in range(15):
    pag.click(x=360, y=678)
    time.sleep(3)
    pag.click(x=784, y=657)
    time.sleep(3)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(25)


