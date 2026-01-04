import time
import pyautogui as pag
from pyautogui import ImageNotFoundException


pag.hotkey('alt', 'tab')
time.sleep(3)

pag.press('down',presses=2)
time.sleep(2)
pag.press('enter')
time.sleep(5)
pag.write('00089127')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write('Cycling@2028')
time.sleep(4)
pag.press('enter')
time.sleep(3)
#

pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nyv209r')
time.sleep(1)
pag.press('enter')
time.sleep(1)
