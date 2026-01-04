import subprocess
import pyautogui as pag
import time



pag.hotkey('alt','tab')
time.sleep(2)
pag.press('tab',presses=5)
time.sleep(1)

n=int((pag.prompt(text='How many days you wish to post cng sales', title='MSG Box' , default='')))

for i in range (n):
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.press('down',presses=4)
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.press('space')
    time.sleep(2)
    pag.press('left')
    time.sleep(2)
    pag.write('c-')
    time.sleep(2)
    pag.press('enter')
    time.sleep(1)
    pag.press('right')
