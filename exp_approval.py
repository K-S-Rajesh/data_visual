import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(3)

for i in range(2):   #no of proposals

    for i in range(3):
        pag.press('tab')
        time.sleep(0.25)


    time.sleep(1)
    pag.press('enter')
    time.sleep(10)
    for i in range(5):
        pag.press('tab')
        time.sleep(0.25)
    pag.press('space')
    time.sleep(8)
    pag.write('recommended for approval ')
    time.sleep(1)
    pag.click(x=920, y=991)
    time.sleep(15)
    pag.click(x=1284, y=114)
    time.sleep(5)





