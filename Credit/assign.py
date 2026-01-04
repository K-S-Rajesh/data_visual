import time
import pyautogui as pag
from pyautogui import ImageNotFoundException

pag.hotkey('alt','tab')


cust=[
#"195654",

]
x=len(cust)
for i in range(x):
    pag.press('f7')
    time.sleep(2)
    pag.write(cust[i])
    time.sleep(2)
    pag.press('tab')
    time.sleep(3)
    pag.press('space')
    time.sleep(3)
