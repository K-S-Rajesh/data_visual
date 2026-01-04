import pyautogui as pag
import time
import os
import subprocess


pag.click(x=1532, y=1164)
time.sleep(1)
# pag.click(x=1531, y=1167)
time.sleep(1)
pag.click(x=1475, y=1018)#if two rows in system tray
# pag.click(x=1462, y=951)#if three rows in system tray
time.sleep(0.25)
pag.doubleClick(x=827, y=663)
time.sleep(1)
pag.write('00089127')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.write('Cycling@2030')
time.sleep(0.25)
pag.press('tab')
time.sleep(0.25)
pag.press('enter')
time.sleep(5)
pag.write(pag.prompt(text='Enter OTP', title='', default=''))
time.sleep(0.25)
pag.press('tab')
time.sleep(0.25)
pag.press('enter')

os.system('start sapshcut.exe -system=PRD -client=310')
time.sleep(10)
# pag.hotkey('alt','space')
# time.sleep(0.3)
# pag.press('x')
