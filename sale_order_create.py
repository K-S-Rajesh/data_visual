import webbrowser
import pyautogui as pag
import time


pag.hotkey('alt','tab')
time.sleep(2)
i=1
while i<=1:
    #im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("indenting.png", confidence=0.7)
        pag.doubleClick(x,y)
        time.sleep(1)
        #pag.click(x, y)
        time.sleep(2)
    except TypeError:
        i = 1
    else:
        break

time.sleep(1)
i=1
while i<=1:
    #im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("contract_indenting.png", confidence=0.7)
        pag.click(x,y)
        time.sleep(1)
        #pag.click(x, y)
        time.sleep(2)
    except TypeError:
        i = 1
    else:
        break

time.sleep(1)
pag.press('tab',presses=4)
time.sleep(1)
pag.write('t94')
time.sleep(1)
pag.press('tab')
time.sleep(2)
pag.write((pag.prompt(text='Enter RO code', title='MSG Box' , default='')),interval=0.3)
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(5)
pag.click(688,514)
time.sleep(2)
pag.press('down')
time.sleep(2)
pag.press('enter')

for i in range(5):
    pag.press('tab')
    time.sleep(0.3)

time.sleep(2)
pag.press('enter')
time.sleep(2)
pag.press('tab',presses=3)


 




