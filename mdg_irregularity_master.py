import webbrowser
import pyautogui as pag
import time

pag.hotkey('alt', 'tab')

for i in range(5):
    time.sleep(1)
    pag.press('up')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.hotkey('alt','down')
    time.sleep(1)
    pag.press('down',presses=14)
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('under hold due to court case')
    time.sleep(0.5)
    pag.press('tab',presses=2)
    time.sleep(0.5)
    pag.press('space')
    time.sleep(3)
    pag.press('enter')
    time.sleep(3)
    pag.press('tab')




