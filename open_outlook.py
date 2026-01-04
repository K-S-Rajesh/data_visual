import os
import time
import pyautogui as pag


os.startfile("outlook")
time.sleep(15)
pag.write('Vagus@123')
time.sleep(1)
pag.press('enter')
pag.hotkey('alt','space')
time.sleep(0.3)
pag.press('x')



