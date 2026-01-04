import pyautogui as pag
import subprocess
import time
import os
import sys

#subprocess.run('C:\\Users\\ksraj\\OneDrive\\Desktop\\saplogon.bat',shell=True)

os.system('start sapshcut.exe -system=PRD -client=310 -user=00501203 -pw=Epicon@456')
time.sleep(40)
pag.hotkey('alt','space')
time.sleep(1)
pag.press('x')
time.sleep(3)

pag.hotkey('ctrl','/')
#pag.press('enter')
pag.write('/nyvr437')
time.sleep(2)
pag.press('enter')
time.sleep(1)
pag.press('tab',presses=3)
time.sleep(1)
pag.write('KER')
time.sleep(1)
pag.press('tab',presses=2)
time.sleep(1)
pag.write('4200')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write((pag.prompt(text='Enter customer code', title='MSG Box' , default='')))
time.sleep(1)
pag.press('f8')

sys.exit()

