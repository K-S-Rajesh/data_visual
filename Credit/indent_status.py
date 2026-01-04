import subprocess
import pyautogui as pag
import time
import os
from datetime import date
from datetime import date,datetime,timedelta

import subprocess

# command = "C:\\Program Files (x86)\\SAP\\sapgui_start.bat"
# try:
#     result = subprocess.run(command, check=True, capture_output=True, text=True)
#     print(result.stdout)
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")
#
# #os.system("")
# time.sleep(10)
pag.hotkey('alt', 'tab')
today=date.today()
# time.sleep(3)
today=date.today()
print(today.strftime("%d.%m.%y"))
from_date=today-timedelta(days=3)
to_date=today+timedelta(days=3)
print(from_date.strftime("%d.%m.%y"))
print(to_date.strftime("%d.%m.%y"))

#
#
# pag.press('down',presses=2)
# time.sleep(2)
# pag.press('enter')
# time.sleep(5)
# pag.write('00501203')
# time.sleep(1)
# pag.press('tab')
# time.sleep(1)
# pag.write('Frontal@123')
# time.sleep(4)
# pag.press('enter')
# time.sleep(3)
# #

#subprocess.run('C:\\Users\\00501203\\OneDrive\\Desktop\\saplogon.bat',shell=True)
#time.sleep(60)
#pag.hotkey('alt','tab')
#time.sleep(5)
# pag.press('x')
time.sleep(5)
pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nva05')
time.sleep(2)
pag.press('enter')
time.sleep(2)
for i in range(7):
    pag.hotkey('shift','tab')
    time.sleep(0.5)

time.sleep(3)
pag.press('enter')
time.sleep(2)
pag.write('4200')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.write('re')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.write('mh')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.write('4203')
time.sleep(2)
pag.press('tab')
time.sleep(2)
#pag.write('')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('enter')
time.sleep(2)
for i in range(3):
    pag.press('tab')
    time.sleep(1)

time.sleep(1)
pag.press('del',presses=10)
time.sleep(1)
pag.write(from_date.strftime("%d.%m.%y"))
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('del',presses=10)
time.sleep(1)
pag.write(to_date.strftime("%d.%m.%y"))
#for i in range(3)
#    pag.press('tab')
time.sleep(1)
pag.press('enter')
time.sleep(45)
# pag.press('alt')
# time.sleep(1)
# pag.press('down',presses=4)
# time.sleep(4)
# pag.press('right')
# time.sleep(4)
# pag.press('down',presses=2)
# time.sleep(4)
# pag.press('enter')
# time.sleep(15)
# pag.press('down')
# time.sleep(4)
# pag.press('enter')
# time.sleep(4)
# pag.press('del',presses=5)
# time.sleep(10)
# pag.write('indent_status.xlsx')
# time.sleep(4)
# pag.press('tab',presses=3)
# time.sleep(4)
# pag.press('enter')
#

pag.rightClick(x=110, y=371)
time.sleep(1)
pag.press('s',presses=2)
time.sleep(1)
pag.press('enter')
time.sleep(5)
pag.press('enter')
time.sleep(10)
pag.press('enter')
time.sleep(3)
pag.press('tab')
time.sleep(2)
pag.press('enter')










