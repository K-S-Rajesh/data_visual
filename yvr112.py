import pyautogui as pag
import subprocess
import time
import os

#subprocess.run('C:\\Users\\ksraj\\OneDrive\\Desktop\\saplogon.bat',shell=True)

os.system('start sapshcut.exe -system=PRD -client=310 -user=00500230 -pw=Iocl@032024')
time.sleep(15)
pag.hotkey('alt','space')
time.sleep(1)
pag.press('x')
time.sleep(3)

pag.hotkey('ctrl','/')
#pag.press('enter')
pag.write('/nyvr112')
time.sleep(2)
pag.press('enter')
#sys.exit()
time.sleep(2)
pag.write('4100')
time.sleep(2)
pag.press('down',presses=5)
time.sleep(1)
pag.write('T94')
time.sleep(2)
pag.press('down')
pag.press('enter')
time.sleep(2)
pag.press('down',presses=2)
time.sleep(1)
pag.press('space')
time.sleep(2)
pag.hotkey('shift','tab')
time.sleep(2)
pag.press('down',presses=4)
time.sleep(2)
pag.press('F8')
time.sleep(2)
sys.exit()
pag.press('alt')
time.sleep(2)
pag.press('down',presses=3)
time.sleep(2)
pag.press('right')
time.sleep(2)
pag.press('down')
time.sleep(2)
pag.press('enter')
time.sleep(2)
pag.press('enter')
time.sleep(4)
pag.press('tab',presses=2)
time.sleep(4)
pag.press('enter')
time.sleep(4)
pag.hotkey('shift','tab')
time.sleep(2)
pag.press('enter')
time.sleep(4)
pag.press('enter')












