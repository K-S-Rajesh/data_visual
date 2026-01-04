import pyautogui as pag
import subprocess
import time
import os
import sys

pag.hotkey('alt', 'tab')
time.sleep(2)

pag.press('tab')
time.sleep(0.3)
pag.write('06 07 2024')
time.sleep(0.3)
pag.press('tab', presses=2)
time.sleep(0.3)
pag.write('06 07 2024')
time.sleep(0.3)
pag.press('tab', presses=2)
time.sleep(0.3)
pag.press('space')
time.sleep(5)
time.sleep(2)
pag.press('enter')
pag.write(pag.prompt(text='Should i continue', title='', default=''))
time.sleep(5)
pag.press('tab', presses=2)
time.sleep(1)
pag.write('complied')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(3)
pag.click(x=1412, y=237)
time.sleep(1)
