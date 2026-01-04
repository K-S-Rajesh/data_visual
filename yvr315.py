import pyautogui as pag
import subprocess
import time
import os
import sys

#subprocess.run('C:\\Users\\ksraj\\OneDrive\\Desktop\\saplogon.bat',shell=True)

os.system('start sapshcut.exe -system=PRD -client=310 -user=00501203 -pw=Epicon@789')
time.sleep(40)
pag.hotkey('alt','space')
time.sleep(1)
pag.press('x')
time.sleep(3)

pag.hotkey('ctrl','/')
#pag.press('enter')
pag.write('/nyvr315')
time.sleep(2)
pag.press('enter')
#sys.exit()
time.sleep(2)
pag.press('tab',presses=6)
time.sleep(1)
pag.write('4203')
time.sleep(1)
pag.press('f8')
time.sleep(10)
pag.press('alt')
time.sleep(1)
pag.press('down',presses=3)
time.sleep(4)
pag.press('right')
time.sleep(4)
pag.press('down')
time.sleep(4)
pag.press('enter')
time.sleep(15)
pag.press('enter')
time.sleep(4)
pag.press('up')
time.sleep(2)
pag.press('enter')
time.sleep(4)
pag.press('tab')
time.sleep(4)
pag.press('enter')
time.sleep(4)
# pag.hotkey('shift','tab')
# time.sleep(4)
# pag.press('enter')
# time.sleep(4)
# pag.hotkey('shift','tab')
# time.sleep(4)
# pag.press('enter')
#
#
#




