import pyautogui as pag
import time


pag.hotkey('alt','tab')
time.sleep(2)

for i in range(6):
    time.sleep(.5)
    pag.press('tab')
time.sleep(.3)


pag.write((pag.prompt(text='Enter date of solarization', title='MSG Box' , default='')))
time.sleep(.3)
for i in range(1):
    time.sleep(.5)
    pag.press('tab')
time.sleep(.3)
pag.write('0.1')
for i in range(3):
    time.sleep(.5)
    pag.press('tab')
time.sleep(.3)
pag.write('0.06')
for i in range(4):
    time.sleep(.5)
    pag.press('tab')
time.sleep(.3)
pag.press('space')
time.sleep(4)
pag.press('enter')
