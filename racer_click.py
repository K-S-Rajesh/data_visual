import webbrowser
import pyautogui as pag
import time




pag.hotkey('alt','tab')
time.sleep(2)
a, b = pag.locateCenterOnScreen("racer.png", confidence=0.7)
pag.click(a, b)
time.sleep(3)
#c, d = pag.locateCenterOnScreen("racer1.png", confidence=0.7)
#pag.click(c, d)
#time.sleep(3)
#pag.scroll(50)
#time.sleep(10)
pag.click(x=166, y=420)
time.sleep(1)