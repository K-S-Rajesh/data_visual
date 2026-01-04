import webbrowser
import pyautogui as pag
import time
import os

pag.hotkey('alt','tab')
time.sleep(1)

pag.press('tab')
time.sleep(0.3)
pag.press('space')
time.sleep(1)
pag.press('F2')
time.sleep(1)

for i in range(5):
    pag.press('tab')
    time.sleep(0.1)

pag.write((pag.prompt(text='Enter MS tank', title='MSG Box' , default='')))

for i in range(9):
    pag.press('tab')
    time.sleep(0.1)

pag.write((pag.prompt(text='Enter HSD tank', title='MSG Box' , default='')))

for i in range(5):
    pag.press('tab')
    time.sleep(0.1)

pag.press('space')

time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.press('tab')

time.sleep(1)
pag.press('enter')
time.sleep(3)
pag.press('enter')
