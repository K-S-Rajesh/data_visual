import pyautogui as pag
import time


pag.hotkey('alt','tab')
time.sleep(1)
for j in range(12):
    i=1
    while i<=1:
            #im = pag.screenshot("Full screen.png")
            try:
                res= pag.locateOnScreen("elec_compl.png", confidence=0.7)
               # print(res)
                action_but=pag.center(res)
                pag.click(action_but)
                #pag.click(x,y)
            except TypeError:
                i = 1
            else:
                break

    time.sleep(8)
    pag.press('enter')
    time.sleep(3)
    pag.press('pageup')
    time.sleep(1)
    pag.click(x=1327, y=614)
    time.sleep(2)
    n=int((pag.prompt(text='How many points to be complied', title='MSG Box' , default='')))
    time.sleep(2)

    for i in range(n):
        pag.press('y')
        time.sleep(1)
        pag.press('tab')
        time.sleep(1)
        pag.write('complied')
        time.sleep(1)
        pag.press('tab')
        time.sleep(1)
        pag.press('space')
        time.sleep(2)
        pag.press('space')
        time.sleep(2)
        pag.press('tab')

    pag.press('space')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(5)

