import webbrowser
import pyautogui as pag
import time

webbrowser.open("https://spandan.indianoil.co.in/RetailNew/Login.jsp")
time.sleep(3)
i=1
while i<=1:
    #im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("rdbscreen.png", confidence=0.7)
    except TypeError:
        i = 1
    else:
        break




pag.press('tab')
time.sleep(1)
pag.write('00507892')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('backspace',presses=14)
time.sleep(1)
pag.write('KANNUR@2024')
time.sleep(1)
pag.press('tab',presses=2)
pag.write((pag.prompt(text='Enter the capcha', title='MSG Box' , default='')))
time.sleep(0.3)
pag.press('tab')
time.sleep(0.3)
pag.press('space')
time.sleep(3)


i=1
while i<=1:
    #im = pag.screenshot("Full screen.png")
    try:
        x, y = pag.locateCenterOnScreen("cross.png", confidence=0.7)
        pag.click(x,y)
    except TypeError:
        i = 1
    else:
        break



