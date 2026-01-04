import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(1)


# Delivery check
for i in range(18):
    j = 1
    while j <= 1:
        # im = pag.screenshot("Full screen.png")
        try:
            res = pag.locateOnScreen("select_surprise_insp.png", confidence=0.7)
            # print(res)
            select_but = pag.center(res)
            pag.click(select_but)
            # pag.click(x,y)
        except TypeError:
            j = 1
        else:
            break

    pag.press('y')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('y')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('c')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('0')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('checked and found ok ')
    time.sleep(10)
    #
    # time.sleep(2)
