import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(1)

# Facility Inspection
for i in range(10):

    j=1
    while j<=1:
        #im = pag.screenshot("Full screen.png")
        try:
            res= pag.locateOnScreen("select_surprise_insp.png", confidence=0.7)
           # print(res)
            select_but=pag.center(res)
            pag.click(select_but)
            #pag.click(x,y)
        except TypeError:
            j = 1
        else:
            break

    time.sleep(1)
    pag.press('down')
    time.sleep(1)
    pag.press('enter')
    # k = 1
    # while k <= 1:
    #     # im = pag.screenshot("Full screen.png")
    #     try:
    #         res = pag.locateOnScreen("save.png", confidence=0.7)
    #         # print(res)
    #         save_but = pag.center(res)
    #         pag.click(save_but)
    #         # pag.click(x,y)
    #     except TypeError:
    #         k = 1
    #     else:
    #         break
    time.sleep(5)






