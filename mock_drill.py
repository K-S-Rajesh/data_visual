import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(1)


for i in range(2):

    i=1
    while i<=1:
        #im = pag.screenshot("Full screen.png")
        try:
            res= pag.locateOnScreen("action.png", confidence=0.7)
           # print(res)
            action_but=pag.center(res)
            pag.click(action_but)
            #pag.click(x,y)
        except TypeError:
            i = 1
        else:
            break

    pag.click(865,618)
    time.sleep(1)
    pag.write('Approved')
    time.sleep(2)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.press('space')
    time.sleep(3)

