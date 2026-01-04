import subprocess
import pyautogui as pag
import time



pag.hotkey('alt','tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write((pag.prompt(text='Enter start date', title='MSG Box' , default='')))
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write((pag.prompt(text='Enter completion date', title='MSG Box' , default='')))
time.sleep(1)
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(10)
pag.press('tab',presses=2)
time.sleep(1)
pag.write('complied')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')

