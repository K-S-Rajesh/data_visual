import pyautogui as pag
import time


pag.hotkey('alt','tab')
time.sleep(1)

for i in range(28):


    i=1
    while i<=1:
       #im = pag.screenshot("Full screen.png")
       try:
         x, y = pag.locateCenterOnScreen("add.png", confidence=0.6)
         pag.click(x,y)
         time.sleep(2)
       except TypeError:
         i = 1
       else:
         break
    time.sleep(2)
    pag.scroll(-30)
    time.sleep(1)

    i=1
    while i<=1:
       #im = pag.screenshot("Full screen.png")
       try:
         x, y = pag.locateCenterOnScreen("search.png", confidence=0.6)
         pag.click(x,y)
         time.sleep(2)
       except TypeError:
         i = 1
       else:
         break
    i=1
    while i<=1:
       #im = pag.screenshot("Full screen.png")
       try:
         x, y = pag.locateCenterOnScreen("customer.png", confidence=0.6)
         pag.click(x,y)
       except TypeError:
         i = 1
       else:
         break
    i=1
    while i<=1:
       #im = pag.screenshot("Full screen.png")
       try:
         x, y = pag.locateCenterOnScreen("ok.png", confidence=0.7)
         pag.click(x,y)
       except TypeError:
         i = 1
       else:
         break
    time.sleep(1)
    pag.press('tab',presses=5)
    time.sleep(1)
    i=1
    while i<=1:
       #im = pag.screenshot("Full screen.png")
       try:
         x, y = pag.locateCenterOnScreen("search.png", confidence=0.6)
         pag.click(x,y)
       except TypeError:
         i = 1
       else:
         break

    time.sleep(10)
    # for j in range(5):
    #    pag.press('tab')
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.press('enter')
    time.sleep(5)
    pag.scroll(30)




