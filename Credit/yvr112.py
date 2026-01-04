import time
import pyautogui as pag
from pyautogui import ImageNotFoundException


pag.hotkey('alt', 'tab')
time.sleep(3)
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

pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nyvr112')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.write('4200')
time.sleep(1)

for i in range(6):
    pag.press('tab')
    time.sleep(1)
time.sleep(1)
pag.write('4203')
time.sleep(1)
for i in range(9):
    pag.press('tab')
time.sleep(1)
pag.press('down',presses=4)
time.sleep(1)
pag.press('f8')
time.sleep(2)
pag.hotkey('ctrl','shift','f7')
